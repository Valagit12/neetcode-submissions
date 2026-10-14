class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = set()

        l, r = 0, 0
        output = 1

        while r < len(s):
            ch = s[r]
            print(seen)
            if ch in seen:
                seen.remove(s[l])
                l+=1
            else:
                seen.add(ch)
                r+=1
            output = max(output, r - l)
        
        return output