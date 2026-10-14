# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        ans = 0
        # frame = [node, left_height, right_height]
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
                ans = max(ans, lh + rh)
                h = 1 + (lh if lh > rh else rh)

                stack.pop()
                if stack:
                    parent = stack[-1]
                    if parent[1] is None:
                        parent[1] = h
                    else:
                        parent[2] = h

        return ans

            
            
#6
'''

4 2 True
3 2 False
2 1 True 
'''
        




            

        


            




        