# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        soln = 0
        
        def recurse(root, depth = 1):
            nonlocal soln
            if not root:
                return 0
            
            left = recurse(root.left, depth + 1)
            right = recurse(root.right, depth + 1)
            soln = max(soln, left + right)

            return max(left, right) + 1
        
        recurse(root)

        return soln

            

        


            




        