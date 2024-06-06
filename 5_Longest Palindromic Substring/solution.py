# Solution Info
# Runtime: 61 ms, faster than 99.10% of Python3 submissions.
# Memory: 16.74 MB, less than 28.49% of Python3 submissions.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        highest = 0
        highest_str = ""
        low = (s_len // 2) - 1
        high = s_len // 2
        if s_len % 2 == 1:
            # Odd Length
            idx = s_len // 2
            i = 1
            count = 1
            while (idx - i) >= 0:
                if s[idx - i] == s[idx + i]:
                    count += 2
                    i += 1
                else:
                    break
            if count > highest:
                highest = count
                i -= 1
                highest_str = s[idx - i : idx + i + 1]
            high += 1
        # Even Length
        iteration_left = low  # aka Remaining Iteration
        while (iteration_left >= 0) and (highest <= ((iteration_left * 2) + 1)):
            # Checking through each character starting from center, both left and right half alternating
            # Therefore, if highest >= 2(iteration_left), no need check for larger palindromic substring

            # [LEFT]
            i = 1
            count = 1
            while (low - i) >= 0:
                if s[low - i] == s[low + i]:
                    count += 2
                    i += 1
                else:
                    break
            if count > highest:
                highest = count
                i -= 1
                highest_str = s[low - i : low + i + 1]

            # [LEFT] Even Palindrome
            if low != 0:
                if s[low] == s[low - 1]:
                    # Left
                    i = 1
                    count = 2
                    while ((low - 1 - i) >= 0) and ((low + i) < s_len):
                        if s[low - 1 - i] == s[low + i]:
                            count += 2
                            i += 1
                        else:
                            break
                    if count > highest:
                        highest = count
                        i -= 1
                        highest_str = s[low - 1 - i : low + i + 1]
            if s[low] == s[low + 1]:
                # Right
                i = 1
                count = 2
                while ((low - i) >= 0) and ((low + 1 + i) < s_len):
                    if s[low - i] == s[low + 1 + i]:
                        count += 2
                        i += 1
                    else:
                        break
                if count > highest:
                    highest = count
                    i -= 1
                    highest_str = s[low - i : low + i + 2]

            low -= 1

            # [RIGHT]
            i = 1
            count = 1
            while (high + i) < s_len:
                if s[high - i] == s[high + i]:
                    count += 2
                    i += 1
                else:
                    break
            if count > highest:
                highest = count
                i -= 1
                highest_str = s[high - i : high + i + 1]

            # [RIGHT] Even Palindrome
            if high != s_len - 1:
                if s[high] == s[high + 1]:
                    # Right
                    i = 1
                    count = 2
                    while ((high - i) >= 0) and ((high + 1 + i) < s_len):
                        if s[high - i] == s[high + 1 + i]:
                            count += 2
                            i += 1
                        else:
                            break
                    if count > highest:
                        highest = count
                        i -= 1
                        highest_str = s[high - i : high + i + 2]
            if s[high] == s[high - 1]:
                # Left
                i = 1
                count = 2
                while ((high - 1 - i) >= 0) and ((high + i) < s_len):
                    if s[high - 1 - i] == s[high + i]:
                        count += 2
                        i += 1
                    else:
                        break
                if count > highest:
                    highest = count
                    i -= 1
                    highest_str = s[high - 1 - i : high + i + 1]

            high += 1

            iteration_left -= 1
        return highest_str
