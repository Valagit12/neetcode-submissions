# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isWordEnd = False
    
#     def addWord(self, word: str) -> None:
#         trie = self
#         for c in word:
#             if c not in trie.children:
#                 trie.children[c] = TrieNode()
#             trie = trie.children[c]
    
#     def visualize(self):
#         trie = self
#         out = {}
#         for c in trie.children.keys():
#             out[c] = trie.children[c].visualize()
                
#         return out

    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Given a string s and a dictionary of strings wordDict
        return true if s can be segmented into a space-separated sequence of dict words
        you are allowed to reuse words in the dictionary an unlimited number of times.

                                                                            applepenapple
                                apple                                               pen                         apex
                    apple       pen            apex             apple               penx        apex
        applex pen apex    apple penx apex                apple penx apex

        applepenapple
                ^
        10000100100001

        dp has a length of 14
        s has a length of 13
        1 + 12 <= 14 

        '''

        dp = [False for i in range(len(s) + 1)] #correct
        dp[-1] = True   #correct

        for i in range(len(s) - 1, -1, -1): #correct
            for word in wordDict: #correct
                if len(word) + i <= len(dp):
                    if word == s[i:i+len(word)]:
                        dp[i] = True and dp[i + len(word)]
                if dp[i] == True:
                    break
        
        return dp[0]
                    






        