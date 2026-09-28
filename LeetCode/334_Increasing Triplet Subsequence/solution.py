class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        minVal = float("inf")
        midVal = float("inf")
        for num in nums:
            if num <= minVal:
                minVal = num
            elif num <= midVal:
                midVal = num
            else:
                return True
        return False

