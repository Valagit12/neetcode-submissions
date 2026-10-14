# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        1 2 3 4
        -

        2 1 3 4
        -


        limit = infinity

                    (1)
                



        '''
        preidx = inidx = 0
        def dfs(limit):
            print(limit)
            nonlocal preidx, inidx
            # case if we are done the tree
            if preidx >= len(preorder):
                return None
            # case if we are done the branch
            if inorder[inidx] == limit:
                inidx+=1
                return None

            node = TreeNode(preorder[preidx])
            preidx += 1
            node.left = dfs(node.val)
            node.right = dfs(limit)
            return node

        
        
        
        return dfs(1000)
        
        