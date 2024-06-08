class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            return int(s)
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
                    elif char == "+":
                        sign = 1
                    else:
                        state = 2
                if state == 2:
                    if char.isdigit():
                        int_length += 1
                    else:
                        break
            if int_length > 0:
                if sign == 0:
                    return int(s[leading_whitespace : leading_whitespace + int_length])
                else:
                    return sign * int(
                        s[leading_whitespace + 1 : leading_whitespace + int_length + 1]
                    )


solution = Solution()
print(solution.myAtoi("42") == -42)  # -42
