# Solution Info (Bodging Method)
# Failed to solve the problem @ 299/356 test cases
# Reason:       Way too complex using current method to fix the remaining issues
# Solution:     Use some form of recursive Decision Tree to solve the problem
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""
        p_index = 0
        remaining_s = s
        while remaining_s != "":
            if p_index >= len(p):
                # s does not match p
                if remaining_s == "":
                    if p_index == len(p):
                        return True
                    else:
                        return False
                return False
            curr_match = p[p_index]
            next_match = ""
            neccessaryCount = 0
            p_index += 1
            if p_index < len(p):
                if p[p_index] == "*":
                    curr_match += "*"
                    p_index += 1
                    while p_index < len(p):
                        if p[p_index] == curr_match[0]:
                            neccessaryCount += 1
                            p_index += 1
                        else:
                            next_match = p[p_index]
                            break
            print(
                f"curr_match: {curr_match}, next_match: {next_match}, remaining_s: {remaining_s}"
            )
            count = 0
            if curr_match == ".*":
                if next_match == "":
                    if p_index == len(p):
                        return True
                    else:
                        return False
                else:
                    while remaining_s != "":
                        if remaining_s[0] == next_match:
                            break
                        remaining_s = remaining_s[1:]
                        count += 1
            else:
                if len(curr_match) == 2:
                    while remaining_s != "":
                        if remaining_s[0] != curr_match[0]:
                            break
                        remaining_s = remaining_s[1:]
                        count += 1
                else:
                    print(f"remaining_s: {remaining_s}")
                    print(f"curr_match: {curr_match}")
                    print(p_index)
                    if remaining_s[0] != curr_match and curr_match != ".":
                        return False
                    remaining_s = remaining_s[1:]
            print(count, neccessaryCount)
            if count < neccessaryCount:
                return False
        # All of s is matching
        if p_index == len(p):
            return True
        else:
            return False


# Test Case example that the current solution failed at:
s = Solution()
print(s.isMatch("aaa", "ab*a*c*a"))

# Side Note:    I am impressed at how far I was able to get with this bodging method of solving each test cases as it fails
#               However, this sort of method is not sustainable for complex problems like these.
