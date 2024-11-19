# Solution Info (DFS [Function Stack] Approach):
# Runtime: 30 ms, faster than 93.22% of Python3 submissions.
# Memory: 16.66 MB, less than 95.79% of Python3 submissions.
def generateParenthesis(self, n: int) -> List[str]:
    results = []

    def dfs(curr: str, brace: int, num_open_brace: int):
        # 1 = "(", 2 = ")"
        nonlocal n, results
        if len(curr) == (2 * n) - 1:
            if brace == 2:
                if num_open_brace == n:
                    # Close (Final - Leaf)
                    results.append(curr + ")")
        else:
            if brace == 1:
                # Open
                dfs(curr + "(", 1, num_open_brace + 1)
                dfs(curr + "(", 2, num_open_brace + 1)
            else:
                # Close
                dfs(curr + ")", 1, num_open_brace)
                if (len(curr) + 2 - num_open_brace) <= num_open_brace:
                    dfs(curr + ")", 2, num_open_brace)

    dfs("", 1, 0)
    return results
