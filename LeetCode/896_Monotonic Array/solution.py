class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        if nums == sorted_nums or nums == sorted_nums[::-1]:
            return True
        else:
            return False
