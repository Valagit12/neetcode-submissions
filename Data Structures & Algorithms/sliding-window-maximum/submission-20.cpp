class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        /**
        1 2 1 4 2 6

        [1 2 5]

        */
        std::deque<int> deq;

        std::vector<int> ans(nums.size() - k + 1);

        int l = 0;
        int ansc = 0;
        for (int r = 0; r < nums.size(); ++r) {
            int num = nums[r];

            while (deq.size() && nums[deq[deq.size() - 1]] < num) {
                deq.pop_back();
            }
            deq.push_back(r);

            if (l > deq[0]) deq.pop_front();

            if (r + 1 >= k) {
                ans[ansc] = nums[deq[0]];
                l++;
                ansc++;
            }
        }
        return ans;


    }
};
