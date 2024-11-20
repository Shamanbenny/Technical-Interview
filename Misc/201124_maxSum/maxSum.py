"""
Problem: Maximum Possible Value at Index k with Constraints

You are given an array of size nn and need to find the maximum possible value at the k-th index of the array while adhering to the following conditions:

Constraints:

    The absolute difference between consecutive elements of the array must be at most 1. That is, for any element arr[i], the absolute difference between it and the next element arr[i+1] must satisfy ∣arr[i+1]−arr[i]∣≤1.
    The total sum of the array elements must not exceed a given value maxSum.

Task:

Write a function maxSum(n, max, k) that takes the following inputs:

    n: The number of elements in the array.
    max: The maximum total sum that the array's elements can have.
    k: The index (1-based) at which you need to find the maximum possible value for that element.

The function should return the maximum possible value that can be placed at index k while ensuring that the sum of the entire array does not exceed maxSum and the absolute difference between consecutive elements is at most 1.

Example:

n = 5
max = 15
k = 3
print(maxSum(n, max, k))  # Output: 4

Explanation:

In this example, the array size is 5, the total sum cannot exceed 15, and we want to find the maximum value that can be placed at index 3. The valid array that satisfies all constraints might look like [3, 4, 4, 3, 2], with a total sum of 15. Hence, the value at index 3 is 4, which is the maximum possible value under the given conditions.
"""
# Complete the 'maxSum' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER max
#  3. INTEGER k
def maxSum(n, max, k):
    # Write your code here
    assert 1 <= k <= n <= max <= 1000000000
    
    def check(x):
        def summ(k):
            return (k*(k+1))//2

        def sumx(k):
            if x <= k:
                sum1 = summ(x) + k - x
            else:
                sum1 = summ(x) - summ(x - k)
            return sum1
        
        ans = sumx(k) + sumx(n - k + 1) - x
        return ans <= max
    
    lo = 1
    hi = max + 1
    while hi - lo > 1:
        mid = (hi + lo)//2
        if check(mid):
            lo = mid
        else:
            hi = mid
    return lo

n = 4
max = 4
k = 3
print(maxSum(n, max, k))