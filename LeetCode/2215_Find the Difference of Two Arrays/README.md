# Find the Difference of Two Arrays

Given two 0-indexed integer arrays `nums1` and `nums2`, return a list `answer` of size 2. `answer[0]` contains all distinct integers in `nums1` not present in `nums2`; `answer[1]` contains all distinct integers in `nums2` not present in `nums1`. The integers may be returned in any order.

### Examples

- Input: `nums1 = [1,2,3]`, `nums2 = [2,4,6]`; Output: `[[1,3],[4,6]]`
- Input: `nums1 = [1,2,3,3]`, `nums2 = [1,1,2,2]`; Output: `[[3],[]]`

### Constraints

- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`

Difficulty: Easy  
Topics: Array, Hash Table  
URL: https://leetcode.com/problems/find-the-difference-of-two-arrays/
