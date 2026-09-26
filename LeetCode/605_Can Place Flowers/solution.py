class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 1:
                continue
            canPlace = True
            if idx - 1 >= 0 and flowerbed[idx - 1] == 1:
                canPlace = False
            if idx + 1 < len(flowerbed) and flowerbed[idx + 1] == 1:
                canPlace = False
            if canPlace:
                flowerbed[idx] = 1
                n -= 1
            if n == 0:
                return True
        return False
