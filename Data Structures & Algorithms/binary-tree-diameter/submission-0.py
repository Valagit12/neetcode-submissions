# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def idfs(root):
            
            if not root:
                return 0
            diameter = 0
            queue = deque()
            queue.append((root, False))

            diameters = {}

            while queue:
                node, visited = queue.pop()
                

                if not visited:
                    queue.append([node, True])
                    if node.right:
                        queue.append([node.right, False])
                    if node.left:
                        queue.append([node.left, False])
                else:
                    left_h = diameters.get(node.left, 0)
                    right_h = diameters.get(node.right, 0)

                    diameter = max(diameter, left_h + right_h)
                    diameters[node] = 1 + max(left_h, right_h)
            
            return diameter
                

        return idfs(root)

