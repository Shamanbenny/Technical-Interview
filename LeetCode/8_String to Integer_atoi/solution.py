# Solution Info
# Runtime: 24 ms, faster than 99.31% of Python3 submissions.
# Memory: 16.47 MB, less than 94.27% of Python3 submissions.
class Solution:
    def myAtoi(self, s: str) -> int:
        def boundCheck(x: int) -> int:
            if x < -2147483648:
                return -2147483648
            elif x > 2147483647:
                return 2147483647
            else:
                return x

        try:
            result = int(s)
            return boundCheck(result)
        except ValueError:
            leading_whitespace = 0
            sign = 0  # 1 for positive, -1 for negative
            int_length = 0
            state = 0  # 0 for leading whitespace, 1 for sign, 2 for integer
            for char in s:
                if state == 0:
                    if char == " ":
                        leading_whitespace += 1
                    else:
                        state = 1
                if state == 1:
                    if char == "-":
                        sign = -1
                        state = 2
                        continue
                    elif char == "+":
                        sign = 1
                        state = 2
                        continue
                    state = 2
                if state == 2:
                    if char.isdigit():
                        int_length += 1
                    else:
                        break
            if int_length > 0:
                result = 0
                if sign == 0:
                    result = int(
                        s[leading_whitespace : leading_whitespace + int_length]
                    )
                else:
                    result = sign * int(
                        s[leading_whitespace + 1 : leading_whitespace + int_length + 1]
                    )
                return boundCheck(result)
            return 0


solution = Solution()
print(solution.myAtoi("  -0012a42"))
