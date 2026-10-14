class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def computeEuc(x1, y1, x2 = 0, y2 = 0):
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5
        
        heap = []

        for x, y in points:
            heapq.heappush(heap, [-computeEuc(x, y), x, y])

            print(heap)
            while len(heap) > k:
                heapq.heappop(heap)
        
        return [[x,y] for _, x, y in heap]
