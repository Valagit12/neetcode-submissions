class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;

        // 3 4 5 6

        
        // 7 - 4 = 3
        // 7 - 3 = 4
        // 7 - 5 = 2
        // 7 - 6 = 1

        for (int i = 0; i < nums.size(); ++i) {
            int num = nums[i];
            if (seen.count(num))
                return {seen[num], i};
            
            seen[target - num] = i;
        }

        return {0, 0};










    }
};
