# Can Place Flowers

You have a long flowerbed in which some plots are planted and some are not. Flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing `0`s and `1`s, and an integer `n`, return `true` if `n` new flowers can be planted without violating the no-adjacent-flowers rule, and `false` otherwise.

## Examples

```text
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
```

```text
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
```

## Constraints

- `1 <= flowerbed.length <= 2 * 10^4`
- `flowerbed[i]` is `0` or `1`.
- There are no two adjacent flowers in `flowerbed`.
- `0 <= n <= flowerbed.length`

Difficulty: Easy

Topics: Array, Greedy

[LeetCode problem](https://leetcode.com/problems/can-place-flowers/)
