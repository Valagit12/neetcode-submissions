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

        def iterative(head):
            if not head:
                return None
            nonlocal nodes
            
            curr = head
            copy = Node(curr.val)
            nodes[head] = copy
            ans = copy

            while curr.next:
                copy.next = Node(curr.next.val)
                nodes[curr.next] = copy.next
                copy = copy.next  
                curr = curr.next
            
            curr = ans
            while head:
                ans.random = nodes.get(head.random)
                ans = ans.next
                head = head.next
            
            return curr
        
        def recursive(head):
            nonlocal nodes
            if not head:
                return None
            
            copy = Node(head.val)
            nodes[head] = copy
            copy.next = recursive(head.next)
            copy.random = nodes.get(head.random)

            return copy
        
        return recursive(head)

            

