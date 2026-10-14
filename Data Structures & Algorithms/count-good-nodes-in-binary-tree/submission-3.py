# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        queue = deque([[root, root.val]])

        while queue:
            node, prevmax = queue.popleft()

            if node.val >= prevmax:
                prevmax = node.val
                count += 1
            
            if node.left:
                queue.append([node.left, prevmax])
            if node.right:
                queue.append([node.right, prevmax])
        

        return count

        