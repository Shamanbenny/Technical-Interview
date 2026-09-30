# Determine if Two Strings Are Close

Two strings are close if one can be attained from the other by swapping any two existing characters and by transforming every occurrence of one existing character into another existing character while transforming the other character in the same way. Return whether `word1` and `word2` are close.

### Examples

- Input: `word1 = "abc"`, `word2 = "bca"`; Output: `true`
- Input: `word1 = "a"`, `word2 = "aa"`; Output: `false`
- Input: `word1 = "cabbba"`, `word2 = "abbccc"`; Output: `true`

### Constraints

- `1 <= word1.length, word2.length <= 10^5`
- Both strings contain only lowercase English letters.

Difficulty: Medium  
Topics: Hash Table, String, Sorting, Counting  
URL: https://leetcode.com/problems/determine-if-two-strings-are-close/
