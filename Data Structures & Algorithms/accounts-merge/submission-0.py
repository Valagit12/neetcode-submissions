class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(set)
        emailToIdx = {}

        for i, a in enumerate(accounts):
            adj[accounts[i][1]]
            emailToIdx[accounts[i][1]] = i
            for j in range(2, len(a)):
                emailToIdx[accounts[i][j]] = i
                adj[accounts[i][j]].add(accounts[i][j-1])
                adj[accounts[i][j-1]].add(accounts[i][j])
        

        visited = set()
        account = []
        def dfs(node):
            account.append(node)
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    dfs(child)

        ans = []
        for key in adj.keys():
            if key not in visited:
                dfs(key)
                account.sort()
                ans.append([accounts[emailToIdx[key]][0]] + account)
                account = []

        return ans
        

