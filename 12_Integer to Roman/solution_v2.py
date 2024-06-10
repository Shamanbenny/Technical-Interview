# Solution Info (Directly converting each digit to its corresponding roman value)
# Runtime: 37 ms, faster than 94.04% of Python3 submissions.
# Memory: 16.48 MB, less than 87.63% of Python3 submissions.
class Solution:
    def intToRoman(self, num: int) -> str:
        # Constraints: 1 <= num <= 3999
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousands = ["", "M", "MM", "MMM"]

        return (
            thousands[num // 1000]
            + hundreds[(num % 1000) // 100]
            + tens[(num % 100) // 10]
            + ones[num % 10]
        )


# Side note:    This approach assumes that the input number is always within the range of 1 to 3999.
#               And that the input number is always limited by its constraints.
#               Therefore, in my opinion, this approach does not provide any visible improvement to its time efficiency,
#               but contains the drawback of being less flexible. (Hard-coding required)
