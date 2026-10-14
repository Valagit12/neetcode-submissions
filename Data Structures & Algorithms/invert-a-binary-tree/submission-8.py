# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive_dfs(root):
            if not root:
                return
            
            if root.left:
                recursive_dfs(root.left)
            if root.right:
                recursive_dfs(root.right)
            
            root.left, root.right = root.right, root.left
        
        recursive_dfs(root)
        return root
            
