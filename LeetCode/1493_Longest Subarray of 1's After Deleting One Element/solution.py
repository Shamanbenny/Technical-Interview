class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        start = 0
        count = 0
        maxCount = 0
        for end in range(len(nums)):
            if nums[end] == 1:
                count += 1
            while end - start + 1 > count + 1:
                if nums[start] == 1:
                    count -= 1
                start += 1
            if (end - start + 1) == count:
                maxCount = max(maxCount, count - 1)
            else:
                maxCount = max(maxCount, count)
        return maxCount
