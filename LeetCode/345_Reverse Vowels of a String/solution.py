class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = set("aeiouAEIOU")
        left = 0
        right = len(s) - 1
        s_list = list(s)
        while left < right:
            if s_list[left] not in vowel:
                left += 1
            if s_list[right] not in vowel:
                right -= 1
            if left < right and s_list[left] in vowel and s_list[right] in vowel:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)
