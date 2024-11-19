# Solution Info (Mathematics Approach)
# Runtime: 53 ms, faster than 50.48% of Python3 submissions.
# Memory: 16.68 MB, less than 65.28% of Python3 submissions.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        currRow = 0
        result = ""

        # Pre-loop calculation
        charPerLoop = 2 * (numRows - 1)
        noOfLoop = len(s) // (charPerLoop)
        charOnLastLoop = charPerLoop
        if len(s) % (charPerLoop) != 0:
            noOfLoop += 1
            charOnLastLoop = len(s) % (charPerLoop)

        # Print Debug
        print(s, numRows)
        print(charPerLoop, noOfLoop, charOnLastLoop)

        # O(n) where n is the len(s)
        while currRow < numRows:
            if currRow == 0:
                # First Row
                for i in range(noOfLoop):
                    result += s[i * charPerLoop]
            elif currRow == numRows - 1:
                # Last Row
                for i in range(noOfLoop):
                    if (i != noOfLoop - 1) or (
                        (i == noOfLoop - 1) and (charOnLastLoop >= numRows)
                    ):
                        result += s[currRow + i * charPerLoop]
            else:
                # Every row inbetween the first and last
                for i in range(noOfLoop):
                    if i != noOfLoop - 1:
                        # NOT last loop
                        result += s[(currRow) + i * charPerLoop]
                        result += s[(charPerLoop - currRow) + i * charPerLoop]
                    else:
                        if charOnLastLoop >= currRow + 1:
                            result += s[(currRow) + i * charPerLoop]
                        if charOnLastLoop >= (charPerLoop - currRow + 1):
                            result += s[(charPerLoop - currRow) + i * charPerLoop]
            currRow += 1
        return result
