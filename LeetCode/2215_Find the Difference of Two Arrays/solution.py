class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        hashmap1 = set(nums1)
        hashmap2 = set(nums2)
        return [list(hashmap1 - hashmap2), list(hashmap2 - hashmap1)]
