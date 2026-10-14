class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0] if len(stones) == 1 else 0
        
        maxheap = [num * -1 for num in stones]
        heapq.heapify(maxheap)
        

        while len(maxheap) > 1:
            x = heapq.heappop(maxheap) * -1
            y = heapq.heappop(maxheap) * -1

            if x == y:
                continue
            else:
                heapq.heappush(maxheap, (x - y) * -1)
        
        return maxheap[0] * -1 if maxheap else 0



        