class TimeMap {
private:
    unordered_map<string, vector<pair<string, int>>> map;
public:
    
    void set(string key, string value, int timestamp) {
       map[key].push_back({value, timestamp}); 
    }
    
    string get(string key, int timestamp) {
        const std::vector<pair<string, int>> &nums = map[key];
        int l = 0; int r = nums.size() - 1;

        string currbest = "";
        while (l <= r) {
            int mid = (l + r) / 2;

            int elem = nums[mid].second;

            if (elem == timestamp) return nums[mid].first;
            else if (elem > timestamp) r = mid - 1;
            else {
                l = mid + 1;
                currbest = nums[mid].first;
            }
        }
        return currbest;
    }
};
