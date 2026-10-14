class Solution {
public:
    string minWindow(string s, string t) {
        if (s.size() < t.size()) return "";
        
        int sizet = t.size();

        unordered_map<char, int> smap;
        unordered_map<char, int> tmap;


        for (int i = 0; i < t.size(); ++i) {
            tmap[t[i]] += 1;
        }
        int matches = 0;
        
        pair<int, int> res = {-1, -1};
        int reslen = 0;

        int l = 0;
        for (int r = 0; r < s.size(); ++r) {
            char chr = s[r];

            if (!tmap.count(chr)) continue;

            smap[chr]++;
            if (smap[chr] == tmap[chr]) {
                matches++;
            }

            while (matches == tmap.size()) {
                char leftchar = s[l];
                if (res.first == -1 || r - l + 1 < reslen) {
                    res = {l, r};
                    reslen = r - l + 1;
                }

                if (smap.count(leftchar)) {
                    smap[leftchar]--;
                    if (smap[leftchar] < tmap[leftchar]) {
                        matches--;
                    }
                }
                l++;
            }

        }
        std::cout << res.first << ' ' << res.second;
        return (res.first == -1 ? "" : s.substr(res.first, res.second - res.first + 1));
    }

        // def minWindow(self, s: str, t: str) -> str:
        // if len(t) > len(s):
        //     return ""
        

        // foundt, founds = {}, {}

        // for i in range(len(t)): foundt[t[i]] = foundt.get(t[i], 0) + 1
        
        // matches = 0
        // l = 0

        // res = (None, None)

        // for r in range(len(s)):
        //     char = s[r]

        //     if not char in foundt: continue
            
        //     founds[char] = founds.get(char, 0) + 1
            
        //     if founds[char] == foundt[char]:
        //         matches += 1
            
        //     print(matches)
        //     while matches == len(foundt):
                
        //         leftchar = s[l]
                
        //         if res[0] == None or r - l + 1 < reslen:    
        //             res = (l, r)
        //             reslen = (r - l + 1)

        //         print(matches, res, reslen,s[res[0]:res[1]+1] )
                
        //         if leftchar in founds: 
        //             founds[leftchar] -= 1
        //             if founds[leftchar] < foundt[leftchar]:
        //                 matches -= 1
        //         l+=1




        // return '' if res[0] == None else s[res[0]:res[1]+1]
};
