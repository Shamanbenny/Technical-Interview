class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        import re
        # Using Regex, we can quickly search for a substring
        match = re.search(needle, haystack)
        if match:
            return match.start()
        else:
            return -1
