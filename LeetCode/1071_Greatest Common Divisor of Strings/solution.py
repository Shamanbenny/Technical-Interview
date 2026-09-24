class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        output = ""
        for i in range(1, len(str1)+1):
            isDivisor = True
            for j in range(i, len(str1), i):
                if str1[0:i] != str1[j:j+i]:
                    isDivisor = False
                    break
            if isDivisor:
                for j in range(0, len(str2), i):
                    if str1[0:i] != str2[j:j+i]:
                        isDivisor = False
                        break
            if isDivisor and len(str1[0:i]) > len(output):
                output = str1[0:i]
        return output
