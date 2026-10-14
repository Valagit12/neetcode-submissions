import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        heap = []
        for bucket in frequencies.keys():
            heapq.heappush(heap, (-frequencies[bucket], bucket))


        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        
        return ans