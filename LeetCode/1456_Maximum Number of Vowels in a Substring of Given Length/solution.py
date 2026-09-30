class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        start = 0
        winCount = 0
        maxCount = 0
        for end in range(len(s)):
            if s[end] in vowels:
                winCount += 1
            
            maxCount = max(maxCount, winCount)

            if end - start + 1 == k:
                if s[start] in vowels:
                    winCount -= 1
                start += 1
                
        return maxCount

