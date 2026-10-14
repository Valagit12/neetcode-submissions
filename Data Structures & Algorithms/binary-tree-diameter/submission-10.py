# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        s1 = [root]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

        mp = {None: 0}  # height in nodes
        res = 0
        while s2:
            node = s2.pop()
            left = mp.get(node.left, 0)
            right = mp.get(node.right, 0)
            res = max(res, left + right)
            mp[node] = 1 + max(left, right)

        return res
            
#6
'''

4 2 True
3 2 False
2 1 True 
'''
        




            

        


            




        