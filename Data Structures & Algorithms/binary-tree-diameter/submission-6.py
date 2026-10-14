# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxdiameter = 0

        def diameter(root):
            nonlocal maxdiameter
            if not root:
                return

            depthl = maxdepth(root.left)
            depthr = maxdepth(root.right)
            maxdiameter = max(maxdiameter, depthl + depthr)

            if root.left:
                diameter(root.left)
            elif root.right:
                diameter(root.right)
            

        def maxdepth(root, depth = 1):
            if not root:
                return 0
            
            if root.left:
                return 1 + maxdepth(root.left, depth + 1)
            if root.right:
                return 1 + maxdepth(root.right, depth + 1)
            return 1

        diameter(root)
        return maxdiameter