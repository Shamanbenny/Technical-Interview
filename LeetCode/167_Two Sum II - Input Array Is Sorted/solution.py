class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        leftIdx = 0
        rightIdx = len(numbers) - 1
        while (leftIdx < rightIdx):
            currSum = numbers[leftIdx] + numbers[rightIdx]
            if (target == currSum):
                return [leftIdx+1, rightIdx+1]
            elif (target < currSum):
                rightIdx -= 1
            else:
                leftIdx += 1
        return []
