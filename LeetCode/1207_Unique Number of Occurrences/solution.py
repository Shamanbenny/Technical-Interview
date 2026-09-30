class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr)
        uniqueCounts = set(counts.values())
        return len(counts.keys()) == len(uniqueCounts)
