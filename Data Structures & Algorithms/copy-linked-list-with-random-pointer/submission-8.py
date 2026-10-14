"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.nodes = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return None
        
        copy = Node(head.val)
        self.nodes[head] = copy
        copy.next = self.copyRandomList(head.next)
        copy.random = self.nodes.get(head.random)
        return copy