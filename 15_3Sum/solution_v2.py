# Solution Info (low and high pointer iterator method)
# Runtime: 633 ms, faster than 78.47% of Python3 submissions.
# Memory: 20.56 MB, less than 78.48% of Python3 submissions.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # O(n log n)
        sortedNums = sorted(nums)
        result = []

        # O(n^2)
        for i, currVal in enumerate(sortedNums[:-2]):
            if (i > 0) and sortedNums[i] == sortedNums[i - 1]:
                # Skip over all first value option duplicates
                continue

            low, high = i + 1, len(sortedNums) - 1

            while low < high:
                sum = currVal + sortedNums[low] + sortedNums[high]
                # Side Note:  Use if into elif for better time complexity (Unless necessary to check all conditions)
                if sum < 0:
                    low += 1
                elif sum > 0:
                    high -= 1
                else:
                    result.append([currVal, sortedNums[low], sortedNums[high]])

                    while (low < high) and (sortedNums[low] == sortedNums[low + 1]):
                        low += 1
                    while (low < high) and (sortedNums[high] == sortedNums[high - 1]):
                        high -= 1

                    low += 1
                    high -= 1

        return result
