# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None

        stack = []
        curr = root
        counter = 0

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()

                if node:
                    counter += 1
                    if counter == k:
                        return node.val
                        break

                    curr = node.right
        
        return 2


