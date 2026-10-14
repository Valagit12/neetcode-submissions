# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        queue = deque([[root, -1000, 1000]])

        while queue:
            node, smallestparent, largestparent = queue.popleft()

            if not (smallestparent < node.val and largestparent > node.val):
                return False

            if node.left:
                queue.append([node.left, smallestparent, min(node.val, largestparent)])
            
            if node.right:
                queue.append([node.right, max(node.val, smallestparent), largestparent])
        
        return True

            
        