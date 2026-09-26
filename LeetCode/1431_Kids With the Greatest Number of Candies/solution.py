class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res = []
        maxCandy = max(candies)
        for curr in candies:
            res.append(curr + extraCandies >= maxCandy)
        return res
