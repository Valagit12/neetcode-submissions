class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # assume there are no duplicate flights and no flights from an airport to itself
        #     -> no repeated edges
        #     -> no self loops

        graph = {i: [] for i in range(n)}

        for parent, child, weight in flights:
            graph[parent].append((weight, child))
        
        #plan_cost, plan_length, node
        minheap = [(0, 0, src)]

        # For any given node, min_flights[i] tracks the minimum plan to that node.
        min_flights = [float('inf') for _ in range(n)]

        visited = set()

        while minheap:
            g_cost, plan_length, parent_node = heapq.heappop(minheap)
            print('expanding node', parent_node, minheap, visited)
            
            if parent_node == dst:
                return g_cost
            
            if plan_length > k:
                continue

            if plan_length > min_flights[parent_node]:
                continue
            
            min_flights[parent_node] = plan_length
            
            # plan_length += 1
            


            for edge_weight, child_node in graph[parent_node]:
                # Im trying without checking child_node in visited
                heapq.heappush(minheap, (edge_weight + g_cost, plan_length + 1, child_node))
            
        return -1
        '''

        (0) --5-->(2)-1->(3)
        |          ^         
        1          |
        |          |
        v          |
        (1)--------1   
        '''





        
        
        
