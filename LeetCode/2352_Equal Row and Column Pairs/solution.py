class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        seen = {}
        res = 0
        for row in range(len(grid[0])):
            curr = str(grid[row])
            seen[curr] = seen.get(curr, 0) + 1
        #print(seen)
        for col in range(len(grid[0])):
            curr = "["
            for idx in range(len(grid[0]) - 1):
                curr += str(grid[idx][col]) + ", "
            curr += str(grid[-1][col]) + "]"
            #print(curr)
            if curr in seen:
                res += seen[curr]
        return res
