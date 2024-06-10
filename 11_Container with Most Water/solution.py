# Solution Info
# Runtime: 484 ms, faster than 93.20% of Python3 submissions.
# Memory: 29.40 MB, less than 82.53% of Python3 submissions.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        high, low = (len(height) - 1), 0
        maxArea = min(height[low], height[high]) * (high - low)
        while high > low:
            if height[high] >= height[low]:
                low += 1
            else:
                high -= 1
            if (min(height[low], height[high]) * (high - low)) > maxArea:
                maxArea = min(height[low], height[high]) * (high - low)
        return maxArea


# Side Note:    The solution had a surprising similarity to the two-pointer solution for the 3Sum problem
#               Once I had figure out the similarity, it was very easy to implement the solution
#               Therefore, the difficulty with this problem was figuring out the efficient solution algorithm
