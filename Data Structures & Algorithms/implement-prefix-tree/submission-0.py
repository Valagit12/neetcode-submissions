'''
Prefix tree (trie) is a tree used to efficiently store and retrieve keys in a set of strings
PrefixTree()

void insert(String word) -> puts word into the tree

bool search(string word) -> true if string in word, false otherwise

bool startsWith(string prefix) -> true if there is a string tha has the prefix and false otherwise

word.length >= 1, 
prefix.length <= 1000 -> never search in the trie for anything over length 1000
word and prefix are lowercase


'''
class Node:
    def __init__(self):
        self.isWordEnd = False
        self.children = {}
        # {
        #     'a' : {'p': {'e' : {} }}
        # }


class PrefixTree:

    def __init__(self):
        self.trie = Node()
        

    def insert(self, word: str) -> None:
        cur = self.trie

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isWordEnd = True
       
    def search(self, word: str) -> bool:
        cur = self.trie

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWordEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        