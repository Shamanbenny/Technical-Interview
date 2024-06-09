# Solution Info (Recursive Decision Tree Method)
# Runtime: 9932 ms, faster than 5.01% of Python3 submissions.
# Memory: 16.56 MB, less than 68.04% of Python3 submissions.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recursiveMatch(s_idx: int, p_idx: int) -> bool:
            # Termination condition
            if (s_idx >= len(s)) and (p_idx >= len(p)):
                return True
            if (s_idx < len(s)) and (p_idx >= len(p)):
                return False

            # Recursive condition
            match = (s_idx < len(s)) and (s[s_idx] == p[p_idx] or p[p_idx] == ".")
            if (p_idx + 1 < len(p)) and p[p_idx + 1] == "*":
                if match:
                    return recursiveMatch(s_idx + 1, p_idx) or recursiveMatch(
                        s_idx, p_idx + 2
                    )
                else:
                    return recursiveMatch(s_idx, p_idx + 2)
            if match:
                return recursiveMatch(s_idx + 1, p_idx + 1)
            return False

        if p == "":
            return s == ""
        return recursiveMatch(0, 0)


# Side Note:    The recursive solution is not the most efficient solution to this problem
#               Therefore, the algorithm can be further improved by utilizing Dynamic Programming
