# Max Number of K-Sum Pairs

You are given an integer array `nums` and an integer `k`.

In one operation, you can pick two numbers from the array whose sum equals `k` and remove them from the array.

Return the maximum number of operations you can perform on the array.

## Examples

```text
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4], remove numbers 1 and 4, then 2 and 3.
```

```text
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Remove two 3s. There are no more pairs that sum up to 6.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^9`

Difficulty: Medium

Topics: Array, Hash Table, Two Pointers, Sorting

[LeetCode problem](https://leetcode.com/problems/max-number-of-k-sum-pairs/)
