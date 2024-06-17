# Solution Info (Recursive DFS Solution) [using Function Stack]
# Runtime:30 ms, faster than 86.57% of Python3 submissions.
# Memory: 16.28 MB, less than 99.80% of Python3 submissions.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numpad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        results = []

        def dfs(curr_combination, remaining_digits):
            if len(remaining_digits) == 0:
                results.append(curr_combination)
                return
            else:
                for char in numpad[remaining_digits[0]]:
                    dfs(curr_combination + char, remaining_digits[1:])

        if len(digits) != 0:
            dfs("", digits)
        return results
