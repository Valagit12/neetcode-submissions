class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def computeEuclideanDistance(x1, y1, x2, y2):
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        heap = []

        for point in points:
            x, y = point

            distance = computeEuclideanDistance(x, y, 0, 0)

            heapq.heappush(heap, [distance, x, y])

        ans = []
        for i in range(k):
            ans.append([heap[0][1], heap[0][2]])
            heapq.heappop(heap)
        
        return ans
    
        