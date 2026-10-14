"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        '''
        3 -> 7 -> 4 -> 5
        n.   5.   3.   7

        3 -> 7

        {3: 3, 7:  }
        '''
        def recurse(head):
            if head is None:
                return None
            if head in nodes:
                return nodes[head]
            
            copy = Node(head.val)
            nodes[head] = copy
            copy.next = recurse(head.next)
            copy.random = nodes.get(head.random)
            return copy
        
        return recurse(head)
            
        