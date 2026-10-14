# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def maxDepth(root):
            if not root:
                return 0
            
            left = maxDepth(root.left) + 1
            right = maxDepth(root.right) + 1
            return max(left, right)
        
        stack = [root]

        ans = 0
        while stack:
            node = stack.pop()

            left = maxDepth(node.left)
            right = maxDepth(node.right)

            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

            ans = max(left + right, ans)
        
        return ans

        

