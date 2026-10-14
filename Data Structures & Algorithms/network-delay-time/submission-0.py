class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for sourceNode, childNode, edgeCost in times:
            graph[sourceNode].append((childNode, edgeCost))

        currPathCost = 0 
        startingNode = k
        minheap = [(currPathCost, startingNode)]
        visited = set()

        while minheap:
            g_cost_to_node, parent_node = heapq.heappop(minheap)
            
            if parent_node in visited:
                continue
            
            visited.add(parent_node)
            
            currPathCost = max(currPathCost, g_cost_to_node)

            for child, edge_weight in graph[parent_node]:
                if child not in visited:
                    heapq.heappush(minheap, (g_cost_to_node + edge_weight, child))
        
        return currPathCost if len(visited) == n else -1




        
