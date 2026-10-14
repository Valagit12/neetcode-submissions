# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([[root, None]])

        while queue:
            node, parent = queue.popleft()

            # less = p if p.val < q.val else q
            # more = q if p.val < q.val else p

            if node == p and node == q:
                return parent

            if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
                return node
            
            if p.val == node.val:
                return p
            if q.val == node.val:
                return q      
            
            if node.left:
                queue.append([node.left, node])
            if node.right:
                queue.append([node.right, node])
        
        return root