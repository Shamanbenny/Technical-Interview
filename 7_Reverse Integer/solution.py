# Solution Info
# Runtime: 26 ms, faster than 97.16% of Python3 submissions.
# Memory: 16.42 MB, less than 91.89% of Python3 submissions.
class Solution:
    def reverse(self, x: int) -> int:
        str_x = ""
        if x < 0:
            # Negative
            str_x = "-" + str(x)[1:][::-1]
        else:
            # Positive
            str_x = str(x)[::-1]

        result = int(str_x)
        # Bound Checking
        if (result < -2147483649) or (result > 2147483648):
            result = 0
        return result
