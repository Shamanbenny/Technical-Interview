"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 

EXAMPLE 
Input: "Tact Coa"
Output: True (permutations: "taco cat", "atco eta", etc.) 
"""
def palindromePermutation(input: str) -> bool:
    char_count = {}
    for char in input:
        if char != " ":
            char_count[char.upper()] = char_count.get(char.upper(), 0) + 1
    # Need to check if Palindrome can be formed
    usedOdd = (sum(char_count.values()) % 2 == 0)
    for freq in char_count.values():
        if freq % 2 != 0:
            if usedOdd:
                return False
            else:
                usedOdd = True
    return True

from collections import Counter
def palindromePermutation_Optimal(input: str) -> bool:
    # Normalize the string: uppercase and remove non-alphabetic characters
    input = ''.join(char.upper() for char in input if char.isalpha())

    char_count = Counter(input)

    usedOdd = (sum(char_count.values()) % 2 == 0)
    for freq in char_count.values():
        if freq % 2 != 0:
            if usedOdd:
                return False
            else:
                usedOdd = True
    return True



print('palindromePermutation("Tact Coa"): ' + str(palindromePermutation("Tact Coa")))
print('palindromePermutation("Coo c"): ' + str(palindromePermutation("Coo c")))
print('palindromePermutation("Coa c"): ' + str(palindromePermutation("Coa c")))
print('palindromePermutation("Cc a"): ' + str(palindromePermutation("Cc a")))

print('palindromePermutation_Optimal("Tact Coa"): ' + str(palindromePermutation_Optimal("Tact Coa")))
print('palindromePermutation_Optimal("Coo c"): ' + str(palindromePermutation_Optimal("Coo c")))
print('palindromePermutation_Optimal("Coa c"): ' + str(palindromePermutation_Optimal("Coa c")))
print('palindromePermutation_Optimal("Cc a"): ' + str(palindromePermutation_Optimal("Cc a")))

"""
While both have O(n) time complexity, there are some subtle differences:

Counter Benefits:
    Readability: Counter provides a more concise and expressive way to count items.
    Built-in Optimizations: Counter is implemented in C under the hood (in CPython), making it slightly faster than a pure Python loop in most cases.
    Advanced Features: Offers methods like most_common(), subtraction of counts, and more, which might be useful for other tasks.

Manual Loop Benefits:
    Customization: Manual counting is more flexible and allows you to apply custom logic (like ignoring spaces and converting to uppercase) inline within the loop.
    Dependencies: Does not require importing an external library (useful in constrained environments).
"""