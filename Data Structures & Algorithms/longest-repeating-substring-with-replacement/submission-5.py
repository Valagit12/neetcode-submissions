from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currMax = 0
        res = 0
        l = 0
        seen = defaultdict(int)
        for r in range(len(s)):
            letter = s[r]

            seen[letter] += 1

            currMax = max(currMax, seen[letter])
            
            if (r - l + 1) - k > currMax:
                seen[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res
