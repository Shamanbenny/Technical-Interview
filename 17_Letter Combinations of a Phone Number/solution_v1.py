# Solution Info (Naive Solution)
# Runtime:37 ms, faster than 43.85% of Python3 submissions.
# Memory: 16.48 MB, less than 76.27% of Python3 submissions.
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

        for num in digits:
            if num == "1":
                continue

            if results == []:
                for char in numpad[num]:
                    results.append(char)
            else:
                prev = results
                results = []
                for char in numpad[num]:
                    for x in prev:
                        results.append(x + char)
        return results
