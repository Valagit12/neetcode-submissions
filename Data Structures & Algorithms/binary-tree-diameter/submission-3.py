# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def idfs(root):

            stack = []
            stack.append([root, False])
            
            heights = {}
            
            diameter = 0


            while stack:
                node, visited = stack.pop()

                if visited:
                    res = 0
                    height = 0
                    if node.left:
                        res += heights.get(node.left, 0)
                        height = res
                    if node.right:
                        height = max(heights.get(node.right, 0), height)
                        res += heights.get(node.right, 0)
                    
                    diameter = max(diameter, res)
                    heights[node] = height + 1
                else:
                    stack.append([node, True])
                    if node.left:
                        stack.append([node.left, False])
                    if node.right:
                        stack.append([node.right, False])
            
            return diameter
        
        return idfs(root)

