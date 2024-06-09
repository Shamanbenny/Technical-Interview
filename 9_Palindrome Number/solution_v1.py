# Solution Info
# Runtime: 45 ms, faster than 87.65% of Python3 submissions.
# Memory: 16.26 MB, less than 99.90% of Python3 submissions.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)
