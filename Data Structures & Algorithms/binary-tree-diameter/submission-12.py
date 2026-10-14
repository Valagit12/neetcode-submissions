# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        stack = [[root, None, None]]
        res = 0

        while stack:
            node, leftheight, rightheight = stack[-1]                

            if leftheight is None:
                if node.left:
                    stack.append([node.left, None, None])
                else:
                    stack[-1][1] = 0
            
            elif rightheight is None:
                if node.right:
                    stack.append([node.right, None, None])
                else:
                    stack[-1][2] = 0

            elif leftheight is not None and rightheight is not None:
                node, leftheight, rightheight = stack.pop()
                res = max(leftheight + rightheight, res)
                if stack:
                    if node == stack[-1][0].left:
                        stack[-1][1] = 1+max(leftheight, rightheight)
                    else:
                        stack[-1][2] = 1+max(leftheight, rightheight)
        return res
            

        

'''
        h
    
  d         a

s   
'''