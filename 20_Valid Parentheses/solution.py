# Solution Info (One Pass solution using buffers)
# Runtime: 28 ms, faster than 92.49% of Python3 submissions.
# Memory: 16.42 MB, less than 91.09% of Python3 submissions.
class Solution:
    def isValid(self, s: str) -> bool:
        braces = {"(": ")", "[": "]", "{": "}"}

        stack = []

        for char in s:
            # Open braces
            if char in braces.keys():
                stack.append(char)

            # Close braces
            if char in braces.values():
                if stack == []:
                    # Close braces without corresponding open braces
                    return False
                if braces[stack[-1]] != char:
                    # Close braces does not match the open braces
                    return False
                else:
                    # Close braces matches the open braces
                    stack.pop()

        if stack == []:
            # All open braces have corresponding close braces
            return True
        else:
            # Open braces exists without corresponding close braces
            return False
