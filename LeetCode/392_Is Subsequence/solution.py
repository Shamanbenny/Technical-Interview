class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        idx = 0
        for curr in t:
            if s[idx] == curr:
                idx += 1
                if idx == len(s):
                    return True
        return False
