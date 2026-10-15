class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: [] for word in words for c in word}

        def addToGraph(word1, word2):
            i = 0
            j = 0

            while i < len(word1) and j < len(word2):
                char1, char2 = word1[i], word2[j]

                if char1 != char2:
                    graph[char1].append(char2)
                    return True
                i += 1
                j += 1
            
            if i == len(word1) and j == len(word2):
                return True
            elif i == len(word1):
                return True
            elif j == len(word2):
                return False
        
        if len(words) == 0:
            return ''
        
        for i in range(1, len(words)):
            if not addToGraph(words[i - 1], words[i]):
                return ""
        
        seen = set()
        cycle = set()
        output = ''
        def dfs(curr):
            nonlocal output
            if curr in cycle:
                return False
            if curr in seen:
                return True
            
            cycle.add(curr)
            for child in graph[curr]:
                if not dfs(child):
                    return False
            seen.add(curr)
            cycle.remove(curr)
            output += curr
            return True
        
        for c in graph.keys():
            if not dfs(c):
                return ''
            
        return output[::-1]

        
            



