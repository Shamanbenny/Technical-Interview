# Solution Info (Without using str())
# Runtime: 41 ms, faster than 94.88% of Python3 submissions.
# Memory: 16.44 MB, less than 91.62% of Python3 submissions.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            # Negative numbers are not palindromes
            return False
        temp = x
        reversed_x = 0
        # O(n) where n is the number of digits in x
        while temp != 0:
            reversed_x = reversed_x * 10 + temp % 10
            temp = temp - (temp % 10)
            temp = temp // 10
        return x == reversed_x
