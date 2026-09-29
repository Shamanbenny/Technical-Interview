class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
            curr = nums[left] + nums[right]
            if curr == k:
                left += 1
                right -= 1
                res += 1
            elif curr < k:
                left += 1
            else:
                right -= 1
        return res
