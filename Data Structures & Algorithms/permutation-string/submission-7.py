class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False


        seen1 = [0] * 26
        seen2 = [0] * 26
        matches = 26

        for i in range(len(s1)):
            index1 = ord(s1[i]) - ord('a')
            index2 = ord(s2[i]) - ord('a')

            if seen1[index1] + 1 == seen2[index1]:
                matches += 1
            elif seen1[index1] == seen2[index1]:
                matches -= 1
            seen1[index1]+=1
    
            if seen2[index2] + 1 == seen1[index2]:
                matches += 1
            elif seen2[index2] == seen1[index2]:
                matches -= 1
            seen2[index2]+=1

        print(matches)
        r = len(s1)
        l = 0
        while r < len(s2):
            if matches == 26:
                return True
            
            ch = s2[r]

            rindex = ord(ch) - ord('a')
            print('r', rindex)

            if seen2[rindex] + 1 == seen1[rindex]:
                matches += 1
            elif seen2[rindex] == seen1[rindex]:
                matches -= 1
            seen2[rindex]+=1

            lindex = ord(s2[l]) - ord('a')
            if seen2[lindex] == seen1[lindex]:
                matches -= 1
            elif seen2[lindex] - 1 == seen1[lindex]:
                matches += 1
            print(matches)
            seen2[lindex] -= 1
            r+=1
            l+=1

        return matches == 26

        

        