# Solution Info (2 pointer iterator w/ hashmap lookup method)
# Runtime: 1459 ms, faster than 19.44% of Python3 submissions.
# Memory: 21.22 MB, less than 12.33% of Python3 submissions.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # O(n log n)
        sortedNums = sorted(nums)
        highestIndexDict = dict(zip(sortedNums, range(len(sortedNums))))
        result = set()

        # O(n^2)
        for i, currVal in enumerate(sortedNums[:-2]):
            if (i > 0) and sortedNums[i] == sortedNums[i - 1]:
                # Skip over all first value option duplicates
                continue

            j = i + 1

            while j < len(sortedNums) - 1:
                lookingFor = -(currVal + sortedNums[j])

                if lookingFor in highestIndexDict:
                    if highestIndexDict[lookingFor] > j:
                        result.add(tuple(sorted([currVal, sortedNums[j], lookingFor])))

                while (j < len(sortedNums) - 1) and (
                    sortedNums[j] == sortedNums[j + 1]
                ):
                    # Skip over all second value option duplicates
                    j += 1

                j += 1

        return result
