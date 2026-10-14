class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        std::vector<std::pair<int, int>> vec;
        for (int i = 0; i < position.size(); i++) {
            vec.push_back({position[i], speed[i]});
        }
        std::sort(vec.begin(), vec.end());

        std::vector<double> stack;

        for (int i = vec.size() - 1; i >= 0; --i) {
            double time_taken = (target - vec[i].first) / (double)vec[i].second;

            if (stack.size() >= 1 && stack.back() >= time_taken) continue;
            stack.push_back(time_taken);
        }

        return stack.size();


    }
};
