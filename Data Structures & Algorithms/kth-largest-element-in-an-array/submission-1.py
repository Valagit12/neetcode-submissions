class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        while len(heap) > k:
            heapq.heappop(heap)
            k -= 1
        
        return heap[0]
