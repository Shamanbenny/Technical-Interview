class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = nums[:]
        # O(n log n)
        sortedNums.sort()
        low_idx = 0
        low = 0
        high_idx = len(nums) - 1
        high = 0
        # O(n)
        while sortedNums[low_idx] <= sortedNums[high_idx]:
            sum = sortedNums[low_idx] + sortedNums[high_idx]
            if sum == target:
                low = sortedNums[low_idx]
                high = sortedNums[high_idx]
                break
            else:
                if sum < target:
                    low_idx += 1
                elif sum > target:
                    high_idx -= 1
        low_idx = -1
        high_idx = -1
        currIdx = 0
        # O(n)
        for i in nums:
            if (i == low) or (i == high):
                if low_idx == -1:
                    low_idx = currIdx
                elif high_idx == -1:
                    high_idx = currIdx
            currIdx += 1
        return [low_idx, high_idx]
        # Therefore, Total Time Complexity: O(n log n)
