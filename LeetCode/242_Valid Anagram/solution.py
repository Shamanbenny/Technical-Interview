class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        # Checks if `s` and `t` has the same Frequency Count Set for all of its alphabets
        return Counter(s) == Counter(t)
