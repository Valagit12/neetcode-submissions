# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans

            if not root:
                return 0
            lh = dfs(root.left)
            rh = dfs(root.right)
            ans = max(lh + rh, ans)
            return max(lh, rh) + 1
        dfs(root)
        return ans


            
            

                    
            
            
#6
'''

4 2 True
3 2 False
2 1 True 
'''
        




            

        


            




        