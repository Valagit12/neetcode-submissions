from functools import cache

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

    def visualize(self):
        trie = self
        out = {}

        queue = deque()
        queue.append(trie)

        while queue:
            outputList = {}
            for _ in range(len(queue)):
                node = queue.popleft()

                for child in node.children:
                    outputList.append(child)
                    queue.append(node.children[child])




class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()

        ROWS, COLS = len(board), len(board[0])

        for word in words:
            trie.addWord(word)
        
        seen = set()
        ans = []

        def dfs(i, j, curr, workingWord):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] not in curr.children:
                return
            
            char = board[i][j]

            if (i, j) in seen:
                return

            if curr.children[char].isEnd:
                ans.append(workingWord + char)
                curr.children[char].isEnd = False

            seen.add((i, j))
            dfs(i + 1, j, curr.children[char], workingWord+char)
            dfs(i - 1, j, curr.children[char], workingWord+char)
            dfs(i, j + 1, curr.children[char], workingWord+char)
            dfs(i, j - 1, curr.children[char], workingWord+char)
            seen.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie, '')
        
        return ans