class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            L,R = 0, i - 1
            while L < R:
                if nums[L] + nums[R] > nums[i]:
                    res += R - L
                    R -= 1
                else:
                    L += 1 
        return res   
