class TrieNode:
    def __init__(self):
        self.isWordEnd = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.trie

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWordEnd = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            cur = node

            for i in range(j, len(word)):
                c = word[i]
                if c not in cur.children and not c == '.':
                    return False
                elif c == '.':
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    cur = cur.children[c]
            return cur.isWordEnd

        return dfs(0, self.trie)
        
        
'''   
ap..

        a
    p

    p  e.

    l  x.
 
    e.


'''