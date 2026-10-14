class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        if (piles.size() == 0) return 0;
        if (h < piles.size()) return -1;

        long long l = 1;
        long long r = *max_element(piles.begin(), piles.end());

        long long rate = r;
        long long minrate = INT_MAX;

        while (l <= r) {
            rate = (l + r) / 2;
            cout << l << ' ' << r << endl;

            long long hours = eatBananas(piles, rate);
            if (hours > h) {
                l = rate + 1;
            } else if (hours <= h) {
                cout << rate << endl;
                minrate = min(minrate, rate);
                r = rate - 1; 
            }
        }
        return minrate;
    }

    long long eatBananas(vector<int>& piles, long long rate) {
        if (rate == 0) return -1;
        long long h = 0;

        for (int i = 0; i < piles.size(); ++i) {
            long long num = piles[i];
            h += (num + rate - 1) / rate;
            // cout << h << ' ' << num << ' ' << rate << endl;
        }

        return h;
    }
};
