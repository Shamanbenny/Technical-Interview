class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        start = 0
        winSum = 0
        maxAvg = float("-inf")
        for end in range(len(nums)):
            winSum += nums[end]

            if end - start + 1 == k:
                maxAvg = max(maxAvg, winSum/(end-start+1))
                winSum -= nums[start]
                start += 1
        
        return maxAvg
