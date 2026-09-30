class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for curr in s:
            if curr == '*':
                stack.pop()
            else:
                stack.append(curr)
        return "".join(stack)
