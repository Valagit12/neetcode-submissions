class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        /**
        [1 2 4 6]

        [1 1 2 8]

        [48 24 12 8]
        */
        int n = nums.size();
        std::vector<int> res(n, 1);

        int prefix = 1;
        for (int i = 0; i < nums.size(); i++) {
            res[i] = prefix;
            prefix *= nums[i];
        }

        int postfix = 1;
        for (int i = nums.size() - 1; i >= 0; --i) {
            res[i] *= postfix;
            postfix *= nums[i];
        }

        return res;

    }
};
