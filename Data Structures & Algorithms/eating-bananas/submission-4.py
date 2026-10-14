class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # [ 1 4 3 2 ]
        # k : 1 -> 4 (m):
        #     h = h - ceil 1/ k

        #     h = h - ceil 4 / k

        #     h = h - ceil 3/k

        #     h = h - ceil 2/k

        #     h >= 0 return k


        maxelem = max(piles)

        low = 1
        high = maxelem

        res = 0

        while low <= high:
            
            mid = (low + high) // 2
            hour = h
            for num in piles:
                hour -= math.ceil(num/mid)
            print(mid, low, high, hour)
                
            
            if hour >= 0:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
                