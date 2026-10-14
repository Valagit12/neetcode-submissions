class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        

        foundt, founds = {}, {}

        for i in range(len(t)): foundt[t[i]] = foundt.get(t[i], 0) + 1
        
        matches = 0
        l = 0

        res = (None, None)

        for r in range(len(s)):
            char = s[r]

            if not char in foundt: continue
            
            founds[char] = founds.get(char, 0) + 1
            
            if founds[char] == foundt[char]:
                matches += 1
            
            print(matches)
            while matches == len(foundt):
                
                leftchar = s[l]
                
                if res[0] == None or r - l + 1 < reslen:    
                    res = (l, r)
                    reslen = (r - l + 1)

                print(matches, res, reslen,s[res[0]:res[1]+1] )
                
                if leftchar in founds: 
                    founds[leftchar] -= 1
                    if founds[leftchar] < foundt[leftchar]:
                        matches -= 1
                l+=1




        return '' if res[0] == None else s[res[0]:res[1]+1]


            