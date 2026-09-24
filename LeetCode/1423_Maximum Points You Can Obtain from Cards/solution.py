class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        total = sum(cardPoints)
        if k >= len(cardPoints):
            return total
        maxPoint = 0
        state = 0
        start = 0
        for end in range(len(cardPoints)):
            state += cardPoints[end]

            if end - start + 1 == len(cardPoints) - k:
                maxPoint = max(maxPoint, total - state)
                state -= cardPoints[start]
                start += 1
        return maxPoint
