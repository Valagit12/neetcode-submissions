# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(root, depth = 1):
            if not root:
                return [0, True]
            
            left, leftbalanced = recurse(root.left, depth + 1)
            right, rightbalanced = recurse(root.right, depth + 1)

            if leftbalanced and rightbalanced and abs(left - right) <= 1:
                return [max(left, right) + 1, True]
            return [-1, False]
        
        return recurse(root)[1]



        