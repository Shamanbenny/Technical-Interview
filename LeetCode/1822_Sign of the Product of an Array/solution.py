class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x: int) -> int:
            if x == 0:
                return 0
            elif x > 0:
                return 1
            else:
                return -1

        if 0 in nums:
            return 0
        else:
            neg_count = sum(signFunc(num) for num in nums if signFunc(num) == -1)
            return 1 if neg_count % 2 == 0 else -1

