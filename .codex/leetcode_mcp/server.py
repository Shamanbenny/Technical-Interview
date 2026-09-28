#!/usr/bin/env python3
"""Dependency-free, read-only MCP adapter for LeetCode's GraphQL API."""

from __future__ import annotations

import json
import os
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GRAPHQL_URL = "https://leetcode.com/graphql/"
DOTENV_KEYS = {"LEETCODE_SESSION", "LEETCODE_CSRF_TOKEN"}
REPO_ROOT = Path(__file__).resolve().parents[2]
SYNC_STATE_PATH = REPO_ROOT / "LeetCode" / ".leetcode_sync.json"


def load_repo_dotenv() -> None:
    """Load simple KEY=value pairs from the repository-local .env file."""
    env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
    try:
        with open(env_path, encoding="utf-8") as env_file:
            lines = env_file.readlines()
    except FileNotFoundError:
        return

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        key, separator, value = line.partition("=")
        if not separator or key not in DOTENV_KEYS or key in os.environ:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
            value = value[1:-1]
        os.environ[key] = value


load_repo_dotenv()


def graphql(query: str, variables: dict[str, Any]) -> dict[str, Any]:
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "technical-interview-repo/leetcode-mcp",
        "Referer": "https://leetcode.com/",
    }
    session = os.environ.get("LEETCODE_SESSION")
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN")
    if session:
        headers["Cookie"] = f"LEETCODE_SESSION={session}"
    if csrf:
        headers["Cookie"] = f"{headers.get('Cookie', '')}; csrftoken={csrf}".lstrip("; ")
        headers["x-csrftoken"] = csrf

    body = json.dumps({"query": query, "variables": variables}).encode()
    request = urllib.request.Request(GRAPHQL_URL, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode())
    except urllib.error.HTTPError as exc:
        # LeetCode often returns useful GraphQL validation details in the
        # response body for HTTP 400. Preserve that detail without logging
        # request headers or any credential material.
        response_body = exc.read().decode("utf-8", errors="replace").strip()
        detail = response_body
        try:
            error_payload = json.loads(response_body)
            messages = [
                str(error.get("message", "GraphQL error"))
                for error in error_payload.get("errors", [])
                if isinstance(error, dict)
            ]
            if messages:
                detail = "; ".join(messages)
        except (json.JSONDecodeError, AttributeError):
            pass
        if len(detail) > 500:
            detail = detail[:500] + "..."
        suffix = f": {detail}" if detail else ""
        raise RuntimeError(f"LeetCode returned HTTP {exc.code}{suffix}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach LeetCode: {exc.reason}") from exc

    if payload.get("errors"):
        raise RuntimeError("; ".join(error.get("message", "GraphQL error") for error in payload["errors"]))
    return payload.get("data", {})


def get_problem(title_slug: str) -> dict[str, Any]:
    query = """
    query question($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId questionFrontendId title titleSlug content difficulty
        isPaidOnly topicTags { name slug }
        exampleTestcases
        codeSnippets { lang langSlug code }
      }
    }
    """
    question = graphql(query, {"titleSlug": title_slug}).get("question")
    if not question:
        raise RuntimeError(f"Problem not found: {title_slug}")
    return question


def search_problems(arguments: dict[str, Any]) -> dict[str, Any]:
    query = """
    query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int,
      $filters: QuestionListFilterInput) {
      questionList(categorySlug: $categorySlug, limit: $limit, skip: $skip,
        filters: $filters) {
        totalNum data {
          questionFrontendId title titleSlug difficulty isPaidOnly
          topicTags { name slug }
        }
      }
    }
    """
    filters: dict[str, Any] = {}
    if arguments.get("difficulty"):
        filters["difficulty"] = arguments["difficulty"]
    if arguments.get("tags"):
        filters["tags"] = arguments["tags"]
    if arguments.get("search_keywords"):
        filters["searchKeywords"] = arguments["search_keywords"]
    return graphql(query, {
        "categorySlug": "",
        "limit": min(int(arguments.get("limit", 20)), 50),
        "skip": max(int(arguments.get("skip", 0)), 0),
        "filters": filters,
    }).get("questionList", {})


def get_user_submissions(arguments: dict[str, Any]) -> dict[str, Any]:
    if not os.environ.get("LEETCODE_SESSION"):
        raise RuntimeError("Full submission history requires LEETCODE_SESSION in the MCP environment")
    query = """
    query submissionList($offset: Int!, $limit: Int!, $lastKey: String) {
      submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
        hasNext lastKey submissions {
          id lang memory runtime statusDisplay timestamp title titleSlug url
        }
      }
    }
    """
    return graphql(query, {
        "offset": max(int(arguments.get("offset", 0)), 0),
        "limit": min(int(arguments.get("limit", 50)), 50),
        "lastKey": arguments.get("last_key"),
    }).get("submissionList", {})


def get_latest_submission() -> dict[str, Any] | None:
    """Return the newest submission, avoiding a history scan when unchanged."""
    if not os.environ.get("LEETCODE_SESSION"):
        raise RuntimeError("Full submission history requires LEETCODE_SESSION in the MCP environment")
    query = """
    query latestSubmission {
      submissionList(offset: 0, limit: 1) {
        submissions {
          id lang memory runtime statusDisplay timestamp title titleSlug url
        }
      }
    }
    """
    submissions = graphql(query, {}).get("submissionList", {}).get("submissions", [])
    return submissions[0] if submissions else None


def load_sync_state() -> dict[str, Any]:
    try:
        with SYNC_STATE_PATH.open(encoding="utf-8") as state_file:
            state = json.load(state_file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid LeetCode sync state: {SYNC_STATE_PATH}") from exc
    if not isinstance(state, dict):
        raise RuntimeError(f"Invalid LeetCode sync state: {SYNC_STATE_PATH}")
    return state


def get_sync_batch() -> dict[str, Any]:
    """Fetch only submissions newer than the MCP-owned sync checkpoint."""
    state = load_sync_state()
    checkpoint = state.get("last_submission_timestamp")
    if checkpoint is not None:
        try:
            checkpoint = int(checkpoint)
        except (TypeError, ValueError) as exc:
            raise RuntimeError("LeetCode sync checkpoint timestamp must be an integer") from exc

    latest = get_latest_submission()
    latest_timestamp = int(latest["timestamp"]) if latest else None
    if checkpoint is not None and (latest_timestamp is None or latest_timestamp <= checkpoint):
        return {
            "submissions": [],
            "checkpoint_timestamp": checkpoint,
            "previous_checkpoint_timestamp": checkpoint,
            "has_new_submissions": False,
            "pages_fetched": 1,
        }

    submissions: list[dict[str, Any]] = []
    offset = 0
    pages_fetched = 0
    while True:
        page = get_user_submissions({"offset": offset, "limit": 50})
        page_submissions = page.get("submissions", [])
        submissions.extend(
            submission
            for submission in page_submissions
            if checkpoint is None or int(submission["timestamp"]) > checkpoint
        )
        pages_fetched += 1
        timestamps = [int(submission["timestamp"]) for submission in page_submissions]
        reached_checkpoint = checkpoint is not None and timestamps and min(timestamps) <= checkpoint
        if reached_checkpoint or not page.get("hasNext") or not page_submissions:
            break
        offset += len(page_submissions)

    fetched_timestamps = [int(submission["timestamp"]) for submission in submissions]
    candidate = max(fetched_timestamps, default=latest_timestamp or checkpoint)
    return {
        "submissions": submissions,
        "checkpoint_timestamp": candidate,
        "previous_checkpoint_timestamp": checkpoint,
        "has_new_submissions": bool(submissions),
        "pages_fetched": pages_fetched,
    }


def commit_sync_checkpoint(arguments: dict[str, Any]) -> dict[str, Any]:
    """Atomically persist a successfully completed sync checkpoint."""
    try:
        candidate = int(arguments["last_submission_timestamp"])
    except (KeyError, TypeError, ValueError) as exc:
        raise RuntimeError("last_submission_timestamp must be an integer") from exc

    state = load_sync_state()
    current = state.get("last_submission_timestamp")
    if current is not None and candidate < int(current):
        raise RuntimeError("Cannot move the LeetCode sync checkpoint backwards")

    updated = {
        "last_sync_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "last_submission_timestamp": candidate,
    }
    SYNC_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=SYNC_STATE_PATH.parent, prefix=".leetcode_sync.", delete=False
    ) as temporary:
        json.dump(updated, temporary, indent=2)
        temporary.write("\n")
        temporary_path = Path(temporary.name)
    os.replace(temporary_path, SYNC_STATE_PATH)
    return updated


def get_submission_code(submission_id: str) -> dict[str, Any]:
    if not os.environ.get("LEETCODE_SESSION"):
        raise RuntimeError("LEETCODE_SESSION is required to fetch submission code")
    query = """
    query submissionDetails($submissionId: Int!) {
      submissionDetails(submissionId: $submissionId) {
        id code lang { name } runtime memory statusDisplay timestamp
        question { title titleSlug questionFrontendId }
      }
    }
    """
    details = graphql(query, {"submissionId": int(submission_id)}).get("submissionDetails")
    if not details:
        raise RuntimeError(f"Submission not found: {submission_id}")
    return details


TOOLS = [
    {"name": "search_problems", "description": "Search public LeetCode problems.", "inputSchema": {"type": "object", "properties": {
        "search_keywords": {"type": "string"}, "difficulty": {"type": "string", "enum": ["EASY", "MEDIUM", "HARD"]},
        "tags": {"type": "array", "items": {"type": "string"}}, "limit": {"type": "integer", "default": 20}, "skip": {"type": "integer", "default": 0}
    }}},
    {"name": "get_problem", "description": "Fetch a problem statement and metadata by title slug.", "inputSchema": {"type": "object", "required": ["title_slug"], "properties": {"title_slug": {"type": "string"}}}},
    {"name": "get_user_submissions", "description": "Fetch one page of the authenticated user's submissions, newest first.", "inputSchema": {"type": "object", "properties": {"offset": {"type": "integer", "default": 0}, "limit": {"type": "integer", "default": 50}, "last_key": {"type": "string"}}}},
    {"name": "get_latest_submission", "description": "Fetch only the authenticated user's newest submission.", "inputSchema": {"type": "object", "properties": {}}},
    {"name": "get_sync_batch", "description": "Read the MCP-owned checkpoint and fetch only submissions newer than it. Does not advance the checkpoint.", "inputSchema": {"type": "object", "properties": {}}},
    {"name": "commit_sync_checkpoint", "description": "Atomically advance the MCP-owned checkpoint after repository writes succeed.", "inputSchema": {"type": "object", "required": ["last_submission_timestamp"], "properties": {"last_submission_timestamp": {"type": "integer"}}}},
    {"name": "get_submission_code", "description": "Fetch source code for one authenticated submission.", "inputSchema": {"type": "object", "required": ["submission_id"], "properties": {"submission_id": {"type": "string"}}}},
]


def call_tool(name: str, arguments: dict[str, Any]) -> Any:
    if name == "search_problems":
        return search_problems(arguments)
    if name == "get_problem":
        return get_problem(arguments["title_slug"])
    if name == "get_user_submissions":
        return get_user_submissions(arguments)
    if name == "get_latest_submission":
        return get_latest_submission()
    if name == "get_sync_batch":
        return get_sync_batch()
    if name == "commit_sync_checkpoint":
        return commit_sync_checkpoint(arguments)
    if name == "get_submission_code":
        return get_submission_code(arguments["submission_id"])
    raise RuntimeError(f"Unknown tool: {name}")


def reply(request_id: Any, result: Any = None, error: dict[str, Any] | None = None) -> None:
    response: dict[str, Any] = {"jsonrpc": "2.0", "id": request_id}
    response["error" if error else "result"] = error or result
    sys.stdout.write(json.dumps(response, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def main() -> None:
    for line in sys.stdin:
        if not line.strip():
            continue
        request = json.loads(line)
        request_id = request.get("id")
        if request_id is None:
            continue
        try:
            method = request.get("method")
            if method == "initialize":
                result = {"protocolVersion": request.get("params", {}).get("protocolVersion", "2024-11-05"), "capabilities": {"tools": {}}, "serverInfo": {"name": "technical-interview-leetcode", "version": "0.1.0"}, "instructions": "Read-only LeetCode access. Credentials are loaded internally from the repo-local .env and must never be read, returned, logged, or written by the skill or MCP tools. Never write repository files from the server."}
            elif method == "tools/list":
                result = {"tools": TOOLS}
            elif method == "tools/call":
                params = request.get("params", {})
                value = call_tool(params["name"], params.get("arguments", {}))
                result = {"content": [{"type": "text", "text": json.dumps(value)}]}
            elif method == "ping":
                result = {}
            else:
                raise RuntimeError(f"Unsupported method: {method}")
            reply(request_id, result=result)
        except Exception as exc:
            reply(request_id, error={"code": -32000, "message": str(exc)})


if __name__ == "__main__":
    main()
