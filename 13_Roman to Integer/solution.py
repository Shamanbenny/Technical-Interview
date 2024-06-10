# Solution Info
# Runtime: 34 ms, faster than 97.39% of Python3 submissions.
# Memory: 16.25 MB, less than 99.92% of Python3 submissions.
class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman Subtractive Forms
        romanSubForms = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        romanSubFormKeys = romanSubForms.keys()
        # Roman Symbols
        romanSymbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        romanSymbolKeys = romanSymbols.keys()

        result = 0
        # Check for Roman Subtractive Forms
        for i in romanSubFormKeys:
            if i in s:
                result += romanSubForms[i]
                s = s.replace(i, "", 1)
        # Check for Roman Symbols
        for i in romanSymbolKeys:
            while i in s:
                result += romanSymbols[i]
                s = s.replace(i, "", 1)
        return result
