# Solution Info (low and high pointer iterator w/ hashmap)
# Runtime: 136 ms, faster than 86.61% of Python3 submissions.
# Memory: 20.64 MB, less than 5.01% of Python3 submissions.


# Total Time Complexity: O(n^2)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pairMap = {}
        results = []

        # O(n log n)
        sortedNums = sorted(nums)

        # O(n^2)
        for i in range(len(sortedNums) - 1):
            if (i > 0) and (sortedNums[i] == sortedNums[i - 1]):
                continue
            for j in range(i + 1, len(sortedNums)):
                if (j > i + 1) and (sortedNums[j] == sortedNums[j - 1]):
                    continue
                if sortedNums[i] + sortedNums[j] not in pairMap:
                    pairMap[sortedNums[i] + sortedNums[j]] = [[i, j]]
                else:
                    pairMap[sortedNums[i] + sortedNums[j]].append([i, j])

        # O(n^2)
        for low in range(len(sortedNums) - 1):
            for high in range(low + 1, len(sortedNums)):
                currSum = sortedNums[low] + sortedNums[high]
                if (target - currSum) in pairMap:
                    for currPair in pairMap[target - currSum]:
                        i, j = currPair
                        if (i != low) and (i != high) and (j != low) and (j != high):
                            # All 4 elements are completely distinct...
                            if (
                                sorted(
                                    [
                                        sortedNums[low],
                                        sortedNums[high],
                                        sortedNums[i],
                                        sortedNums[j],
                                    ]
                                )
                                not in results
                            ):
                                results.append(
                                    sorted(
                                        [
                                            sortedNums[low],
                                            sortedNums[high],
                                            sortedNums[i],
                                            sortedNums[j],
                                        ]
                                    )
                                )

        return results
