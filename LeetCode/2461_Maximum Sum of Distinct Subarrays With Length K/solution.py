class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        if k > len(nums):
            return 0
        start = 0
        maxSum = float("-inf")
        windowSum = 0
        count = set()
        for end in range(len(nums)):
            windowSum += nums[end]
            while nums[end] in count:
                windowSum -= nums[start]
                count.remove(nums[start])
                start += 1
            count.add(nums[end])

            if end - start + 1 == k:
                maxSum = max(maxSum, windowSum)
                windowSum -= nums[start]
                count.remove(nums[start])
                start += 1
        return 0 if maxSum == float('-inf') else maxSum
