class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1contains = defaultdict(int)
        s2contains = defaultdict(int)

        for i in range(len(s1)):
            s1contains[s1[i]] += 1
            s2contains[s2[i]] += 1
        
        matches = 26

        for idx in range(26):
            char = chr(idx + ord('a'))
            if s1contains[char] != s2contains[char]:
                matches -= 1

        l = 0
        for r in range(len(s1), len(s2)):
            print(l, r, s2contains)
            if matches == 26:
                return True

            rightChar = s2[r]
            s2contains[rightChar] += 1

            if s2contains[rightChar] == s1contains[rightChar]:
                matches += 1
            elif s2contains[rightChar] == s1contains[rightChar] + 1:
                matches -= 1
            
            leftChar = s2[l]
            s2contains[leftChar] -= 1
            if s2contains[leftChar] == s1contains[leftChar]:
                matches += 1
            elif s2contains[leftChar] == s1contains[leftChar] - 1:
                matches -= 1
            l+=1

        return matches == 26

