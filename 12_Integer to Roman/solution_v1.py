# Solution Info (Greedy Algorithm approach)
# Runtime: 39 ms, faster than 90.25% of Python3 submissions.
# Memory: 16.45 MB, less than 87.63% of Python3 submissions.
class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        romanValues = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        romanValueKeys = list(romanValues.keys())
        subtractiveForms = {900: "CM", 400: "CD", 90: "XC", 40: "XL", 9: "IX", 4: "IV"}
        subtractiveFormKeys = list(subtractiveForms.keys())

        def getRomanValue(num: int) -> tuple[int, str]:
            numStr = str(num)
            if (numStr[0] != "4") and (numStr[0] != "9"):
                for i in romanValueKeys:
                    if num >= i:
                        # Since first digit is not 4 or 9, we can just multiply the roman value appropriately
                        return (
                            num - (num // i) * i,
                            (num // i) * romanValues[i],
                        )
            else:
                for i in subtractiveFormKeys:
                    if num >= i:
                        return (num - i, subtractiveForms[i])

        while num != 0:
            num, roman = getRomanValue(num)
            result += roman
        return result
