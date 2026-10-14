# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root1, root2):
            if (root1 and not root2) or (root2 and not root1):
                return False
            
            if not root1 and not root2:
                return True
            
            if root1.val == root2.val:
                left = isEqual(root1.left, root2.left)
                right = isEqual(root1.right, root2.right)
                if left and right:
                    return True
                return False
            return False
        

        def dfs(root, subroot):
            if not root:
                return False
            
            if not subroot:
                return True
            
            isequal = False
            if root.val == subroot.val:
                isequal = isEqual(root, subroot)
            return isequal or (dfs(root.left, subroot) or dfs(root.right, subroot))
        
        return dfs(root, subRoot)
        