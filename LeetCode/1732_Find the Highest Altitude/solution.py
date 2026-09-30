class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefixSum = [0]
        for curr in gain:
            prefixSum.append(prefixSum[-1] + curr)
        return max(prefixSum)
