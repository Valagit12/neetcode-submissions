# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([[root, 0]])
        bfsorder = []
        while queue:
            node, depth = queue.popleft()
            bfsorder.append([node.val, depth])
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
        
        ans = [[]]
        mostrecentlevel = bfsorder[0][1]
        for val, level in bfsorder:
            if level != mostrecentlevel:
                mostrecentlevel += 1
                ans.append([val])
            else:
                ans[mostrecentlevel].append(val)
        
        return ans


            
            
        