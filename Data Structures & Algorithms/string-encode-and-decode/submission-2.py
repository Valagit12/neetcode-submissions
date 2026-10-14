class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += s +'\n'
        
        return encoded
        

    def decode(self, s: str) -> List[str]:
        return s.split('\n')[0:-1]
