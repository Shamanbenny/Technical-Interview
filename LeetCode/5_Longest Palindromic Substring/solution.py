# Solution Info
# Runtime: 60 ms, faster than 99.12% of Python3 submissions.
# Memory: 16.66 MB, less than 46.81% of Python3 submissions.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        highest = 0
        s_len = len(s)
        highest_str = ""

        def checkPalindrome(
            s: str, start_left: int, start_right: int, start_count: int
        ) -> str:
            i = 1
            count = start_count
            while (start_left - i) >= 0 and (start_right + i) < s_len:
                if s[start_left - i] == s[start_right + i]:
                    count += 2
                    i += 1
                else:
                    break
            i -= 1
            return s[start_left - i : start_right + i + 1]

        low = (s_len // 2) - 1
        high = s_len // 2
        if s_len % 2 == 1:
            # Odd Length
            idx = s_len // 2
            result = checkPalindrome(s, idx, idx, 1)
            if len(result) > highest:
                highest = len(result)
                highest_str = result
            high += 1
        # Even Length
        iteration_left = low  # aka Remaining Iteration
        while (iteration_left >= 0) and (highest <= ((iteration_left * 2) + 1)):
            # Checking through each character starting from center, both left and right half alternating
            # Therefore, if highest >= 2(iteration_left), no need check for larger palindromic substring

            # [LEFT]
            result = checkPalindrome(s, low, low, 1)
            if len(result) > highest:
                highest = len(result)
                highest_str = result

            # [LEFT] Even Palindrome
            if low != 0:
                if s[low] == s[low - 1]:
                    # Left
                    result = checkPalindrome(s, low - 1, low, 2)
                    if len(result) > highest:
                        highest = len(result)
                        highest_str = result
            if s[low] == s[low + 1]:
                # Right
                result = checkPalindrome(s, low, low + 1, 2)
                if len(result) > highest:
                    highest = len(result)
                    highest_str = result

            low -= 1

            # [RIGHT]
            result = checkPalindrome(s, high, high, 1)
            if len(result) > highest:
                highest = len(result)
                highest_str = result

            # [RIGHT] Even Palindrome
            if high != s_len - 1:
                if s[high] == s[high + 1]:
                    # Right
                    result = checkPalindrome(s, high, high - 1, 2)
                    if len(result) > highest:
                        highest = len(result)
                        highest_str = result
            if s[high] == s[high - 1]:
                # Left
                result = checkPalindrome(s, high - 1, high, 2)
                if len(result) > highest:
                    highest = len(result)
                    highest_str = result

            high += 1

            iteration_left -= 1
        return highest_str
