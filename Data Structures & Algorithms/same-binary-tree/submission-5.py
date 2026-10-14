# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recursive(root1, root2):
            if not root1 and not root2:
                return True
            
            if (root1 and not root2) or (root2 and not root1):
                return False
            
            if root1.val == root2.val:
                left = recursive(root1.left, root2.left)
                right = recursive(root1.right, root2.right)
                if not left or not right:
                    return False
                else:
                    return True
            return False
        
        return recursive(p, q)
