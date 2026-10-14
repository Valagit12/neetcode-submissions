class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        currlength, maxlength = 0, 0
        for r in range(0, len(s)):
            if s[r] in seen:
                maxlength = max(r - l, maxlength)
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l+=1
                l += 1

            seen.add(s[r])
        
        return max(maxlength, len(seen))