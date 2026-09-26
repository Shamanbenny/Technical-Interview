# Kids With the Greatest Number of Candies

There are `n` kids with candies. Given an integer array `candies`, where `candies[i]` is the number of candies the `i`th kid has, and an integer `extraCandies`, return a boolean array where each value indicates whether giving all the extra candies to that kid results in the greatest number of candies among all the kids.

Multiple kids can have the greatest number of candies.

## Examples

```text
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
```

```text
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
```

```text
Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
```

## Constraints

- `n == candies.length`
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`

Difficulty: Easy

Topics: Array

[LeetCode problem](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
