# Solution Info
# Runtime: 70 ms, faster than 95.13% of Python3 submissions.
# Memory: 16.74 MB, less than 96.12% of Python3 submissions.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two lists and sort them
        nums = sorted(nums1 + nums2)
        # Find the median index (Right middle index if even, middle index if odd)
        mid = len(nums) // 2
        if len(nums) % 2 == 0:
            # Even
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            # Odd
            return nums[mid]
