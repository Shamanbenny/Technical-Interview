"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

A permutation is a rearrangement of characters.
Two strings are considered permutations of each other if they contain the same characters in the same frequency, 
    regardless of the order.
"""
def isPermutation(string1: str, string2: str) -> bool:
    hash_map = {}
    for char in string1:
        if char in hash_map:
            hash_map[char] += 1
        else:
            hash_map[char] = 1
    for char in string2:
        if char in hash_map:
            hash_map[char] -= 1
            if (hash_map[char] < 0):
                return False
        else:
            return False
    for freq_count in set(hash_map.values()):
        if freq_count != 0:
            return False
    return True

def isPermutation_Optimal(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        # This edge case checks avoids needing to ensure every freq_count is only 0
        return False
    hash_map = {}
    for char in string1:
        hash_map[char] = hash_map.get(char, 0) + 1
    for char in string2:
        if char not in hash_map or hash_map[char] == 0:
            return False
        hash_map[char] -= 1
    return True

print('isPermutation("abc", "cba"): ' + str(isPermutation("abc", "cba")))
print('isPermutation("abc", "cbda"): ' + str(isPermutation("abc", "cbda")))
print('isPermutation("abc", "cbd"): ' + str(isPermutation("abc", "cbd")))
print('isPermutation("abc", "cbd"): ' + str(isPermutation("abc", "cb")))

print('isPermutation_Optimal("abc", "cba"): ' + str(isPermutation_Optimal("abc", "cba")))
print('isPermutation_Optimal("abc", "cbda"): ' + str(isPermutation_Optimal("abc", "cbda")))
print('isPermutation_Optimal("abc", "cbd"): ' + str(isPermutation_Optimal("abc", "cbd")))
print('isPermutation_Optimal("abc", "cbd"): ' + str(isPermutation_Optimal("abc", "cb")))