class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # O(n) Time Complexity, by carrying from reverse linear movement
        n = len(digits)
        for i in range(len(digits)):
            if digits[n - i - 1] == 9:
                digits[n - i - 1] = 0
            else:
                digits[n - i - 1] += 1
                return digits
        return [1] + digits
