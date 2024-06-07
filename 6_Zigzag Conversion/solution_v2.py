# Solution Info (Intuitive Approach)
# Runtime: 43 ms, faster than 90.90% of Python3 submissions.
# Memory: 16.48 MB, less than 99.06% of Python3 submissions.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        # Create a list of strings to store the result
        result = [""] * numRows
        goingDown = True
        currRow = 0

        # O(n) where n is len(s)
        for char in s:
            result[currRow] += char
            if goingDown:
                if currRow != numRows - 1:
                    currRow += 1
                else:
                    # Change the direction
                    currRow -= 1
                    goingDown = False
            else:
                if currRow != 0:
                    currRow -= 1
                else:
                    # Change the direction
                    currRow += 1
                    goingDown = True

        # Reconstruction of the result
        return "".join(result)
