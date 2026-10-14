class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) - 1



        while low < high:
            low_char = s[low].lower()

            if not low_char.isalnum():
                low += 1
                low_char = ord(s[low].lower())
                continue
            
            high_char = s[high].lower()

            if not (high_char.isalnum()):
                high -= 1
                high_char = ord(s[high].lower())
                continue
            

            if low_char != high_char:
                return False
            
            low+=1
            high-=1
            
        return True
            
            




