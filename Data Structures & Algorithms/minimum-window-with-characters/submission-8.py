class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''

        t_counts = {}
        for cr in t:
            t_counts[cr] = t_counts.get(cr, 0) + 1
        
        s_counts = {}
        matches = 0

        
        res = (None, None)

        l = 0
        for r in range(len(s)):
            rightChar = s[r]
            if rightChar not in t_counts:
                continue

            s_counts[rightChar] = s_counts.get(rightChar, 0) + 1
            if s_counts[rightChar] == t_counts[rightChar]:
                matches += s_counts[rightChar]
            
            if matches != len(t):
                continue

            if (res[0] == None) or r - l < res[1] - res[0]:
                res = (l, r)
            
            while True:
                leftChar = s[l]
                l+=1
                print(l)
                if leftChar in t_counts:
                    s_counts[leftChar] -= 1
                    if s_counts[leftChar] < t_counts[leftChar]:
                        matches -= 1
                        break

            if (res[0] == None) or r - l < res[1] - res[0]:
                res = (l-1, r)
            
            
        if res[0] == None:
            return ''
        else:
            return s[res[0]:res[1] + 1]
            