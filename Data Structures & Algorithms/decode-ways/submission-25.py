class Solution:
    def numDecodings(self, s: str) -> int:
        
        '''
                                11261
                (1 1261)                                         (11 261)
    (1 1 262)               (1 12 61)                    (11 2 61)           (11 26 1)
(1 1 2 62) (1 1 26 2).  (1 12 6 1)

        '''

        def dfs(st):
            if not st:  # empty string → 1 valid decoding
                return 1
            if st[0] == "0":  # can't start with 0
                return 0

            # Option 1: decode one digit, recurse on rest
            res = dfs(st[1:])

            # Option 2: decode two digits if valid, recurse on rest
            if len(st) >= 2 and int(st[:2]) <= 26:
                res += dfs(st[2:])
            return res


            
        return dfs(s)
            


