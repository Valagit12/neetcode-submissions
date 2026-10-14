# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def get_gain(node):
            if not node:
                return 0
            
            # Recursively get the max gain from subtrees
            # If the gain is negative, we take 0 (don't include the path)
            left_gain = max(get_gain(node.left), 0)
            right_gain = max(get_gain(node.right), 0)
            
            # Price of a new path: node + left + right
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the max gain this node can contribute to its parent
            return node.val + max(left_gain, right_gain)

        get_gain(root)
        return self.max_sum
        