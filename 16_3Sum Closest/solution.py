# Solution Info (low and high pointer iterator method)
# Runtime: 76 ms, faster than 93.30% of Python3 submissions.
# Memory: 16.50 MB, less than 97.88% of Python3 submissions.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Edge Case: If the length of the nums is 3, return the sum of the elements
        if len(nums) == 3:
            return sum(nums)

        # O(n log n)
        sortedNums = sorted(nums)

        # Edge Case: If the sum of the first 3 sorted elements is greater than the target
        currResultVal = sum(sortedNums[:3])
        if currResultVal >= target:
            return currResultVal

        # Edge Case: If the sum of the last 3 sorted elements is less than the target
        currResultVal = sum(sortedNums[-3:])
        if currResultVal <= target:
            return currResultVal

        # O(n^2)
        currResultVal = sortedNums[0] + sortedNums[1] + sortedNums[2]
        for idx, val in enumerate(sortedNums[:-2]):
            if (val == sortedNums[idx - 1]) and (idx != 0):
                continue

            low, high = idx + 1, len(sortedNums) - 1
            while low < high:
                currSum = val + sortedNums[low] + sortedNums[high]
                if abs(target - currSum) < abs(target - currResultVal):
                    currResultVal = currSum

                if currSum < target:
                    while (low < high) and (sortedNums[low] == sortedNums[low + 1]):
                        low += 1
                    low += 1
                elif currSum > target:
                    while (low < high) and (sortedNums[high] == sortedNums[high - 1]):
                        high -= 1
                    high -= 1
                else:
                    # Found the only combination of exact targets
                    return currSum
        return currResultVal
