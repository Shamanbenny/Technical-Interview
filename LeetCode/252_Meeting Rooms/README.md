# Meeting Rooms

Premium problem

## Description

Write a function to check if a person can attend all the meetings scheduled without any time conflicts. Given an array `intervals`, where each element `[s1, e1]` represents a meeting starting at time `s1` and ending at time `e1`, determine if there are any overlapping meetings. If there is no overlap between any meetings, return `true`; otherwise, return `false`.

Meetings ending and starting at the same time, such as `(0,5)` and `(5,10)`, do not conflict.

## Example 1

Input:

```text
intervals = [(1,5),(3,9),(6,8)]
```

Output:

```text
false
```

Explanation: The meetings `(1,5)` and `(3,9)` overlap.

## Example 2

Input:

```text
intervals = [(10,12),(6,9),(13,15)]
```

Output:

```text
true
```

Explanation: There are no overlapping meetings, so the person can attend all.

Canonical URL: https://leetcode.com/problems/meeting-rooms/
