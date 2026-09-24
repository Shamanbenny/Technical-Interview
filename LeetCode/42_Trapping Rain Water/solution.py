class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        leftHighest = 0
        rightHighest = 0
        while (left <= right):
            if (leftHighest <= rightHighest):
                if height[left] > leftHighest:
                    leftHighest = height[left]
                else:
                    water += (leftHighest - height[left])
                left += 1
            elif (leftHighest > rightHighest):
                if height[right] > rightHighest:
                    rightHighest = height[right]
                else:
                    water += (rightHighest - height[right])
                right -= 1
        return water
