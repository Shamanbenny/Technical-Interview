# Solution Info
# Runtime: 30 ms, faster than 93.59% of Python3 submissions.
# Memory: 16.49 MB, less than 97.37% of Python3 submissions.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge Case
        if len(strs) == 1:
            return strs[0]

        lCP = ""
        # Acquire Longest Common Prefix between first two strings
        for char in strs[0]:
            if strs[1].startswith(lCP + char):
                lCP += char
            else:
                break

        # Edge Case
        if len(strs) == 2:
            return lCP

        for string in strs[2:]:
            if not lCP:
                return lCP
            while not string.startswith(lCP):
                lCP = lCP[:-1]
                if not lCP:
                    return lCP
        return lCP
