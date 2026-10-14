from collections import defaultdict

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     di = defaultdict(int)
    #     di2 = defaultdict(int)
    #     for char in s:
    #         di[char] += 1
        
    #     for char in t:
    #         di2[char] += 1
        
    #     return di == di2
    
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)