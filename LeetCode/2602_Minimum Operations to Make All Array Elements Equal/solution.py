import bisect

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        nums.sort()
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        for target in queries:
            left_idx = bisect_left(nums, target)
            actions = (left_idx * target) - prefix[left_idx]
            actions += (prefix[-1] - prefix[left_idx]) - (target * (len(nums) - left_idx))
            res.append(actions)
        
        return res
        