# Solution Info (Top-Down Memoization Method)
# References: https://www.youtube.com/watch?v=HAA8mgxlov8
# Runtime: 29 ms, faster than 99.06% of Python3 submissions.
# Memory: 16.74 MB, less than 33.95% of Python3 submissions.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def recursiveMatch(s_idx: int, p_idx: int) -> bool:
            # Memoization
            if (s_idx, p_idx) in cache:
                return cache[(s_idx, p_idx)]

            # Termination condition
            if (s_idx >= len(s)) and (p_idx >= len(p)):
                return True
            if (s_idx < len(s)) and (p_idx >= len(p)):
                return False

            # Recursive condition
            match = (s_idx < len(s)) and (s[s_idx] == p[p_idx] or p[p_idx] == ".")
            if (p_idx + 1 < len(p)) and p[p_idx + 1] == "*":
                if match:
                    cache[(s_idx, p_idx)] = recursiveMatch(
                        s_idx + 1, p_idx
                    ) or recursiveMatch(s_idx, p_idx + 2)
                    return cache[(s_idx, p_idx)]
                else:
                    cache[(s_idx, p_idx)] = recursiveMatch(s_idx, p_idx + 2)
                    return cache[(s_idx, p_idx)]
            if match:
                cache[(s_idx, p_idx)] = recursiveMatch(s_idx + 1, p_idx + 1)
                return cache[(s_idx, p_idx)]
            cache[(s_idx, p_idx)] = False
            return cache[(s_idx, p_idx)]

        if p == "":
            return s == ""
        return recursiveMatch(0, 0)
