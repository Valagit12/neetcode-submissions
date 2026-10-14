class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # '''
        #  cat--bat--bag--sag      dot
        #             \    /
        #              dag
        # '''
        def oneApart(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                if diff == 2:
                    return False
            return True

        graph = {}

        # O(n^2 * m) where m is the length of each word and n is the length of wordList
        for i in range(len(wordList)):
            word1 = wordList[i]
            if word1 not in graph:
                graph[word1] = []
            for j in range(len(wordList)):
                if j == i:
                    continue
                word2 = wordList[j]

                if oneApart(word1, word2):
                    graph[word1].append(word2)
        
        graph[beginWord] = []
        for j in range(len(wordList)):
            word = wordList[j]

            if oneApart(beginWord, word):
                graph[word].append(beginWord)
                graph[beginWord].append(word)
        
        queue = deque()
        queue.append((beginWord, 0, []))
        seen = set()

        while queue:
            currNode, currDist, path = queue.popleft()

            if currNode in seen:
                continue

            if currNode == endWord:
                return currDist + 1

            seen.add(currNode)

            for child in graph[currNode]:
                if child not in seen:
                    queue.append((child, currDist + 1, path + [child]))
        
        return 0
                    

            

            


            
