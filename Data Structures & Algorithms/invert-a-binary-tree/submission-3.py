# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None
            
            node.left = dfs(node.left)

            node.right = dfs(node.right)


            node.left, node.right = node.right, node.left
            return node
        

        def bfs(node):
            if not node: return None

            queue = deque()
            queue.append(node)

            while queue:
                node = queue.popleft()
                node.left, node.right = node.right, node.left

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            return root
        
        return bfs(root)
        