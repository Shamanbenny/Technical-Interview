# Solution Info
# Runtime: 51 ms, faster than 76.11% of Python3 submissions.
# Memory: 16.51 MB, less than 91.15% of Python3 submissions.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        substring = ""
        for element in s:
            index = substring.find(element)

            if index == -1:
                # Does not exist in substring
                substring += element
            else:
                # Exist in substring
                # Therefore, "reconstruct" substring starting from after where the existing character is within the substring
                max_len = max(max_len, len(substring))
                substring = substring[index + 1 :] + element
        max_len = max(max_len, len(substring))
        return max_len
