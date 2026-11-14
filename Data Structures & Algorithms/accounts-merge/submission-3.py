class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # email -> children
        adj = {}
        nameToEmail = {}

        for name, *emails in accounts:
            firstEmail = emails[0]
            nameToEmail[firstEmail] = name
            if firstEmail not in adj:
                adj[firstEmail] = set()
            
            for i in range(1, len(emails)):
                email = emails[i]
                nameToEmail[email] = name
                if email not in adj:
                    adj[email] = set()
                adj[email].add(firstEmail)
                adj[firstEmail].add(email)
        
        visited = set()
        def iterativeDfs(startNode: str) -> List[str]:
            stack = [startNode]
            visited.add(startNode)
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for child in adj[node]:
                    if child not in visited:
                        visited.add(child)
                        stack.append(child)
            return sorted(component)

        ans = []
        for node in adj.keys():
            if node not in visited:
                ans.append([nameToEmail[node]] + iterativeDfs(node))
        
        return ans
            





       
        

