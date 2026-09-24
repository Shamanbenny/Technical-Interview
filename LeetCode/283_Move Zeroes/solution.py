class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Naive solution: Following the same principle as Bubble Sort, therefore O(n^2) Time Complexity
        # for i in range(len(nums)):
        #     for j in range(len(nums) - i - 1):
        #         if nums[j] == 0 and nums[j+1] != 0:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        # 2 Pass Solution: O(n) Time Complexity
        curr_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr_idx] = nums[i]
                curr_idx += 1
        for i in range(curr_idx, len(nums)):
            nums[i] = 0
