# Solution Info (Swap with the first previous unique element):
# Runtime: 68 ms, faster than 90.30% of Python3 submissions.
# Memory: 17.78 MB, less than 95.59% of Python3 submissions.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        tmpIdx = 0
        tmpVal = nums[0] - 1
        uniqueCount = 0
        for idx, val in enumerate(nums):
            if val != tmpVal:
                # curr val is unique
                tmpVal = val
                if idx != tmpIdx:
                    # curr val is not in the correct position
                    nums[tmpIdx], nums[idx] = val, nums[tmpIdx]
                tmpIdx += 1
                uniqueCount += 1
        return uniqueCount
