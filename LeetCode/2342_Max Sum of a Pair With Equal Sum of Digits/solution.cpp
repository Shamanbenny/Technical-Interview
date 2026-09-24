class Solution {
public:
    int digitSum(int n) {
        int sum = 0;
        while (n != 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    int maximumSum(vector<int>& nums) {
        // filled with -1; (9 * 9) + 1 possible sum of digits; 2 index of maximum value that makes up the sum of digits.
        int memory[82][2] = {};
        fill(&memory[0][0], &memory[0][0]+82*2, -1);

        int maxSum = -1;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int ds = digitSum(nums[i]);
            if (memory[ds][0] == -1) {
                memory[ds][0] = i;
            } else if (memory[ds][1] == -1) {
                memory[ds][1] = i;
                if ((nums[memory[ds][0]] + nums[memory[ds][1]]) > maxSum) {
                    maxSum = nums[memory[ds][0]] + nums[memory[ds][1]];
                }
            } else {
                // Both indexes are filled with valid index...
                if (nums[memory[ds][0]] <= nums[memory[ds][1]]) {
                    if (nums[memory[ds][0]] < nums[i]) {
                        memory[ds][0] = i;
                        if ((nums[memory[ds][0]] + nums[memory[ds][1]]) > maxSum) {
                            maxSum = nums[memory[ds][0]] + nums[memory[ds][1]];
                        }
                    }
                } else {
                    if (nums[memory[ds][1]] < nums[i]) {
                        memory[ds][1] = i;
                        if ((nums[memory[ds][0]] + nums[memory[ds][1]]) > maxSum) {
                            maxSum = nums[memory[ds][0]] + nums[memory[ds][1]];
                        }
                    }
                }
            }
        }
        return maxSum;
    }
};
