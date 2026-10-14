class Solution {
public:
    bool isAnagram(string s, string t) {
        int val_s[26] = {0};
        int val_t[26] = {0};

        int base = 'a';
        // a = 15, b = 16, c = 17

        for (auto chr : s) {
            int index = chr - base;
            ++val_s[index];
        }

        for (auto chr : t) {
            int index = chr - base;
            ++val_t[index];
        }

        for (int i = 0; i < 26; i++) {
            if (val_s[i] != val_t[i]) {
                return false;
            }
        }
        return true;

        



    }
};
