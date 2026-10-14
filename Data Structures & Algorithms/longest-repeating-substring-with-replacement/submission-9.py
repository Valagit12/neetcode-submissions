class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        output = 0

        if not s:
            return 0
        
        l, r = 0, 0
        maxfreq = 1

        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1
            if seen[s[r]] > maxfreq:
                maxfreq = seen[s[r]]

            while (r - l + 1) - maxfreq > k:
                seen[s[l]] -= 1
                l+=1
            output = max(output, r - l + 1)
            r+=1
            

        return output
        