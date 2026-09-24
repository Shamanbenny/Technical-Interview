from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # If a character exists in both s AND t, then the XOR operation cancels out, 
        #   leaving only the ASCII value of the difference
        xor = 0
        for char in s + t:
            xor ^= ord(char)
        return chr(xor)
