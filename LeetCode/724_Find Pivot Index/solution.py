import bisect

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefixSum = [0]
        for curr in nums:
            prefixSum.append(prefixSum[-1] + curr)
        for idx in range(len(prefixSum) - 1):
            if prefixSum[idx] == prefixSum[-1] - nums[idx] - prefixSum[idx]:
                return idx
        return -1
