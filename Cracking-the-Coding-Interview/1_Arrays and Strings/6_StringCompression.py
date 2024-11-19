"""
String Compression: Implement a method to perform basic string compression using the counts 
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the 
"compressed" string would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and lowercase letters (a - z). 
"""
def stringCompression(input: str) -> str:
    buffer = []
    curr_count = 1
    curr = input[0]
    for char in input[1::]:
        if char != curr:
            buffer.append(curr + str(curr_count))
            curr = char
            curr_count = 1
        else:
            curr_count += 1
    buffer.append(curr + str(curr_count))

    output = "".join(buffer)
    if len(input) <= len(output):
        return input
    else:
        return output
    
print('stringCompression("aabcccccaaa"): ' + stringCompression("aabcccccaaa"))
print('stringCompression("abcaaa"): ' + stringCompression("abcaaa"))
