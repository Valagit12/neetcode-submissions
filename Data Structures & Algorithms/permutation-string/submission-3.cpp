class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) {
            return false;
        }
        
        int s1map[26] = {0};
        int s2map[26] = {0};
        int matches = 26;

        for (int i = 0; i < s1.size(); ++i) {
            ++s1map[s1[i] - 'a'];
            ++s2map[s2[i] - 'a'];
        }

        for (int i = 0; i < 26; ++i) {
            if (s1map[i] != s2map[i]) {
                --matches;
            }
        }

        int l = 0;
        for (int r = s1.size(); r < s2.size(); ++r) {
            if (matches == 26) return true;

            int index = s2[r] - 'a';
            ++s2map[index];
            if (s1map[index] == s2map[index]) {
                ++matches;
            } else if (s1map[index] + 1 == s2map[index]) {
                --matches;
            }

            index = s2[l] - 'a';
            --s2map[index];
            if (s1map[index] == s2map[index]) {
                ++matches;
            } else if (s1map[index] - 1 == s2map[index]) {
                --matches;
            }
            ++l;
        }
        return matches == 26;

    }
};
