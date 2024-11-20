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
def maxSum(n, max, k):
    # Function to check if a given value for arr[k-1] is valid
    def is_valid(mid):
        total_sum = 0
        
        # Fill the array in a way that the sum doesn't exceed max
        # From 0 to k-1 (inclusive), values are decreasing towards arr[k-1]
        for i in range(k-1, -1, -1):
            total_sum += mid - (k-1-i)  # Decreasing to maintain the difference constraint
            if total_sum > max:  # If we exceed max at any point, it's not valid
                return False

        # From k to n-1 (inclusive), values are increasing from arr[k-1]
        for i in range(k, n):
            total_sum += mid + (i-k)  # Increasing to maintain the difference constraint
            if total_sum > max:  # If we exceed max at any point, it's not valid
                return False
        
        return total_sum <= max
    
    # Binary search for the maximum valid value for arr[k-1]
    left, right = 0, max
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if is_valid(mid):
            result = mid  # This value is valid, try for a larger one
            left = mid + 1
        else:
            right = mid - 1
    
    return result

n = 4
max = 4
k = 3
print(maxSum(n, max, k))