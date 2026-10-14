class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::vector<int> res(temperatures.size());// -> [0 0 0 0 ...]
        std::vector<int> stack;

        for (int i = 0; i < res.size(); ++i) {
            while (stack.size() && temperatures[i] > temperatures[stack.back()]) {
                res[stack.back()] = i - stack.back();
                stack.pop_back();
            }
            stack.push_back(i);
        }
        return res;
    }
};
