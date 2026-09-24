# LeetCode

Github SubFolder containing my solution for LeetCode problems

## My account

https://leetcode.com/u/SneakyOwl/

## IMPORTANT

Please note that my solution may not necessarily be the best optimized algorithm, but is instead a representation of my culminated coding capabilities and knowledge.

## Sync solved submissions

This repository includes a repo-local `sync-leetcode` skill and MCP server. In Codex, invoke it with:

```text
/sync-leetcode
```

The skill finds accepted submissions and creates missing problem folders under `LeetCode/`, including the problem README and submitted source code. Existing files are not overwritten.

### One-time setup

1. Copy the example environment file from the repository root:

   ```bash
   cp .env.example .env
   ```

2. Log in to [LeetCode](https://leetcode.com/).

3. Open your browser's developer tools and locate the cookies for `https://leetcode.com`:

   - Chrome/Edge: **Application** → **Storage** → **Cookies** → `https://leetcode.com`
   - Firefox: **Storage** → **Cookies** → `https://leetcode.com`

4. Copy the value of the `LEETCODE_SESSION` cookie into `.env`:

   ```dotenv
   LEETCODE_SESSION=paste_the_cookie_value_here
   # Optional:
   LEETCODE_CSRF_TOKEN=paste_csrftoken_value_here
   ```

   The session cookie is equivalent to an authenticated browser session. Keep it private, do not commit `.env`, and revoke it by signing out of LeetCode or clearing the session if it is exposed.

   The skill and MCP tools load the credentials internally. Do not open, print, copy, or paste `.env` contents into Codex prompts, tool arguments, generated files, or reports.

5. Restart Codex or reload the MCP server, then invoke `/sync-leetcode` whenever you want to synchronize your accepted submissions.
