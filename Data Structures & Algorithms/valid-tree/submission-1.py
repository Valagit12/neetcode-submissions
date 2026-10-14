class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        indegrees = {i: 0 for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            indegrees[a] += 1
            graph[b].append(a)
            indegrees[b] += 1

        '''

        {0: [1, 2, 3], 1: [0, 4], 2: [0], 3: [0]}
        indegrees: {0: 3, 1: 2, 2: 1, 3: 1, 4: 1}


        {0: [1], 1: [0, 2, 4, 3], 2: [1, 3], 3: [1, 2], 4: [1]}

        '''

        if n == 0:
            return True

        queue = deque()
        queue.append((None, 0))

        track = set()
        track.add(0)

        while queue:
            parent, node = queue.popleft()

            for child in graph[node]:
                if child != parent:
                    if child in track:
                        return False
                    queue.append((node, child))
                    track.add(child)
        
        if len(track) < n:
            return False
        
        return True

        

        


        