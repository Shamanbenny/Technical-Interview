class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Set word1 to always be the longer string
        output = []
        max_len = max(len(word1), len(word2))
        for i in range(max_len):
            if i < len(word1):
                output.append(word1[i])
            if i < len(word2):
                output.append(word2[i])
        return "".join(output)

