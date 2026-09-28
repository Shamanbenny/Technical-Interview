---
name: sync-leetcode
description: Sync the user's authenticated LeetCode submissions into this repository's LeetCode folder. Use when asked to sync, import, or update solved LeetCode problems from LeetCode.
---

# Sync LeetCode

Use the repo-local `leetcode` MCP server configured in `mcp.json`.

## Workflow

1. Read `LeetCode/README.md` and inspect existing problem folders under `LeetCode/` before changing anything. The MCP owns `LeetCode/.leetcode_sync.json`; do not read or write that file directly from the skill.
2. Call `get_sync_batch`. It reads the checkpoint, probes the newest submission, and returns only submissions newer than the checkpoint. If `has_new_submissions` is false, stop with no repository changes. Always deduplicate the returned records by `titleSlug` and keep the newest accepted submission for each problem (`statusDisplay == "Accepted"`). Do not treat compile errors, wrong answers, or timeouts as solved entries.
3. Match local problem folders by the numeric prefix before the first underscore (`<questionFrontendId>_`), not by the full title-derived path. This preserves existing folders despite title capitalization, punctuation, suffixes, or renamed titles.
4. For each accepted problem without a local folder, call `get_problem` and `get_submission_code` for the selected submission.
5. Create `LeetCode/<questionFrontendId>_<title>/`, sanitizing unsafe filesystem punctuation while preserving the repository's numeric naming convention.
6. Write `README.md` with the fetched statement, constraints, examples when available, difficulty, topic tags, and canonical URL. Never invent missing content.
7. Write the submitted source as `solution.py`, `solution.js`, `solution.java`, `solution.cpp`, or another extension matching the returned language. Never overwrite an existing README or solution unless the user explicitly asks for refresh/overwrite.
8. After all requested files are written successfully, call `commit_sync_checkpoint` with the returned `checkpoint_timestamp`. The MCP atomically updates `LeetCode/.leetcode_sync.json`; do not advance the checkpoint after an authentication, fetch, or write failure.
9. Report created, skipped-existing, and failed entries, plus the number of submission pages fetched. If authentication is missing, stop without writing partial entries and explain that `LEETCODE_SESSION` must be provided to the MCP process.

## Safety and repository conventions

- The MCP server is read-only with respect to LeetCode data. It owns only the atomic checkpoint write in `LeetCode/.leetcode_sync.json`; this skill owns problem-folder repository writes.
- Never submit code, alter LeetCode data, or expose session cookies in output or committed files.
- Never open, print, summarize, copy, or send `.env` contents. Do not include credentials in MCP arguments, prompts, generated files, or status reports; the MCP server loads them internally.
- Prefer the repository's existing plain `README.md` and `solution*.py` conventions; do not reformat unrelated entries.
- Treat the LeetCode statement as fetched content. Do not add solution explanations, performance claims, or metadata that were not returned by the server.
