# Solution Info (Organized Code)
# Runtime: 53 ms, faster than 87.29% of Python3 submissions.
# Memory: 17.29 MB, less than 95.41% of Python3 submissions.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n log n)
        sortedNums = sorted(nums)

        # O(n)
        low, high = 0, len(sortedNums) - 1
        while low < high:
            sum = sortedNums[low] + sortedNums[high]
            if sum < target:
                while (low < high) and (sortedNums[low] == sortedNums[low + 1]):
                    low += 1
                low += 1
            elif sum > target:
                while (low < high) and (sortedNums[high] == sortedNums[high - 1]):
                    high -= 1
                high -= 1
            else:
                # Found the two numbers
                # Now to acquire their respective original index position
                low = sortedNums[low]
                high = sortedNums[high]
                temp = -1

                # O(n)
                for idx, num in enumerate(nums):
                    if num == low or num == high:
                        if temp == -1:
                            temp = idx
                        else:
                            return [temp, idx]

        # Total Time Complexity: O(n log n)
