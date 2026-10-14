class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                manhattan = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append((manhattan, j))
                graph[j].append((manhattan, i))
        
        res = 0
        visited = set()

        minheap = [(0, 0)]

        while minheap:
            cost, node = heapq.heappop(minheap)

            if node in visited:
                continue
            
            visited.add(node)
            res += cost
            for weight, child in graph[node]:
                if child not in visited:
                    heapq.heappush(minheap, (weight, child))
        
        return res
                
