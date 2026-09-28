class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        numOfZero = 0
        fullProduct = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                numOfZero += 1
                if numOfZero >= 2:
                    return [0] * len(nums)
            else:
                fullProduct = fullProduct * nums[i]
        print(fullProduct)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = fullProduct
            else:
                if numOfZero == 0:
                    nums[i] = int(fullProduct / nums[i])
                else:
                    nums[i] = 0
        
        return nums

