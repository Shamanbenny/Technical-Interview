"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, 
and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.) 
EXAMPLE 
Input:      "Mr John Smith", 13 
Output:     "Mr%20John%20Smith" 
"""
def URLify(string: str, length: int) -> str:
    buffer = []
    for char in string:
        if char == " ":
            buffer.append("%20")
        else:
            buffer.append(char)
    return "".join(buffer)

print('URLify("Mr John Smith", 13): "' + URLify("Mr John Smith", 13) + '"')
print('URLify("testing", 7): "' + URLify("testing", 7) + '"')
print('URLify("Mr John Smith ", 14): "' + URLify("Mr John Smith ", 14) + '"')