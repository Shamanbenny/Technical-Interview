class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        count = ""
        windowStack = []
        window = ""
        for char in s:
            if char.isnumeric():
                # Number
                count += char
            elif char == "[":
                # Open Bracket
                countStack.append(int(count))
                count = ""
                windowStack.append(window)
                window = ""
            elif char != "]":
                # String
                window += char
            else:
                # Close Bracket
                window = windowStack.pop() + "".join([window] * countStack.pop())
        return window

