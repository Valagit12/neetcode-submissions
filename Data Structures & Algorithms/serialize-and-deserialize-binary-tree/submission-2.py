# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    '''
    2 3
    '''
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        queue = deque()
        queue.append(root)

        serialized = ''
        while queue:
            head = queue.popleft()
            
            if head and head.left:
                queue.append(head.left)
            elif head:
                queue.append(None)
            if head and head.right:
                queue.append(head.right)
            elif head:
                queue.append(None)
            
            if head == None:
                serialized+= 'x' + ','
            else:
                serialized += str(head.val) + ','
        return serialized [0:len(serialized) - 1]
        
    # Decodes your encoded data to tree.
    '''
    i*2 +1, i*2 + 2
    1 2 3 4 5 6 7
            1
        2.      3
     4.   5.  6.  7
    '''
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(',')

        root = TreeNode(int(values[0]))
        queue = deque([root])

        i = 1

        while queue:
            node = queue.popleft()

            # Next value belongs to node.left
            if i < len(values):
                if values[i] != 'x':
                    node.left = TreeNode(int(values[i]))
                    queue.append(node.left)
                i += 1

            # Next value belongs to node.right
            if i < len(values):
                if values[i] != 'x':
                    node.right = TreeNode(int(values[i]))
                    queue.append(node.right)
                i += 1

        return root
        