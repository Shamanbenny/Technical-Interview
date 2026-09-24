class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start = 0
        count = 0
        maxLen = 0
        for end in range(len(nums)):
            if nums[end] == 1:
                count += 1
            if count + k < end - start + 1:
                if nums[start] == 1:
                    count -= 1
                start += 1
            maxLen = max(maxLen, end - start + 1)
        return maxLen
