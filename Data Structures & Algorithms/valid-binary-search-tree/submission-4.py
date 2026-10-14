# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def bfs(root):

            queue = deque()
            queue.append([root, float('-inf'), float('inf')])
            while queue:
                    
                node, left, right = queue.pop()

                if not (left < node.val < right):
                    return False

                if node.left:
                    queue.append([node.left, left, node.val])

                if node.right:
                    queue.append([node.right, node.val, right])
            
            return True
        
        return bfs(root)
        