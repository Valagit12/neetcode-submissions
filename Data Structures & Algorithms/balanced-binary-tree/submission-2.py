# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [[root, None, None]]

        while stack:
            node, lh, rh = stack[-1]

            if lh is None:
                if node.left:
                    stack.append([node.left, None, None])
                else:
                    stack[-1][1] = 0
            elif rh is None:
                if node.right:
                    stack.append([node.right, None, None])
                else:
                    stack[-1][2] = 0
            else:
                if abs(lh - rh) > 1:
                    return False
                
                stack.pop()
                if stack:
                    parent = stack[-1]
                    if parent[1] is None:
                        parent[1] = 1 + max(lh, rh)
                    else:
                        parent[2] = 1 + max(lh, rh)
            
        return True





        