# Decode String

Given an encoded string, return its decoded string. The encoding rule is `k[encoded_string]`, where the enclosed string is repeated exactly `k` times. The input is valid, contains no extra whitespace, and the original data does not contain digits.

### Examples

- Input: `s = "3[a]2[bc]"`; Output: `"aaabcbc"`
- Input: `s = "3[a2[c]]"`; Output: `"accaccacc"`
- Input: `s = "2[abc]3[cd]ef"`; Output: `"abcabccdcdcdef"`

### Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets.
- `s` is valid; all integers are in `[1, 300]`.
- The decoded length does not exceed `10^5`.

Difficulty: Medium  
Topics: String, Stack, Recursion  
URL: https://leetcode.com/problems/decode-string/
