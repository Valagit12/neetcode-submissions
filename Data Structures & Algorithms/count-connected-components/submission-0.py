class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        def dfs(node):
            for child in graph[node]:
                if child not in seen:
                    seen.add(child)
                    dfs(child)

        
        count = 0
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                count += 1
        
        return count
        