"""
One Away: There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check if they are 
one edit (or zero edits) away.

EXAMPLE 
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""
from collections import Counter
def oneAway(input: str, to: str) -> bool:
    # This solution would be preferred if permutation is allowed...
    if (input == to):
        return True
    if (abs(len(input) - len(to)) > 1):
        return False
    
    char_count = Counter(to)

    for char in input:
        if char not in char_count:
            char_count[char] = char_count.get(char, 0) - 1
        else:
            char_count[char] -= 1
            if char_count[char] < -1:
                return False
    
    added = False
    removed = False
    for freq in char_count.values():
        if freq > 0:
            if freq > 1:
                return False
            if not added:
                added = True
            else:
                return False
        if freq < 0:
            if not removed:
                removed = True
            else:
                return False
    return True

def oneAway_Optimal(s1: str, s2: str) -> bool:
    if (abs(len(s1) - len(s2)) > 1):
        return False

    # Determine which is shorter and which is longer
    if len(s1) > len(s2):
        s1, s2 = s2, s1  # Ensure s1 is the shorter string
    index1 = 0
    index2 = 0
    difference = False
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if difference:
                return False
            difference = True
        
            if len(s1) != len(s2):
                index2 += 1
                continue
        index1 += 1
        index2 += 1
    return True

print('oneAway("pale", "ple"): ' + str(oneAway("pale", "ple")))
print('oneAway("pales", "pale"): ' + str(oneAway("pales", "pale")))
print('oneAway("pale", "bale"): ' + str(oneAway("pale", "bale")))
print('oneAway("pale", "bake"): ' + str(oneAway("pale", "bake")))

print('oneAway_Optimal("pale", "ple"): ' + str(oneAway_Optimal("pale", "ple")))
print('oneAway_Optimal("pales", "pale"): ' + str(oneAway_Optimal("pales", "pale")))
print('oneAway_Optimal("pale", "bale"): ' + str(oneAway_Optimal("pale", "bale")))
print('oneAway_Optimal("pale", "bake"): ' + str(oneAway_Optimal("pale", "bake")))