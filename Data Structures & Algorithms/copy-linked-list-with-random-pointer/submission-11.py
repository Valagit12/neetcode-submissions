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
        curr = head

        dummy = Node(0)
        dup = dummy

        while curr:
            
            dup.next = Node(curr.val, None, curr.random)

            nodes[curr] = dup.next

            curr = curr.next

            dup = dup.next
            
        
        print(nodes)
        
        while head:
            nodes[head].random = nodes.get(head.random, None)

            head = head.next
        

        
        return dummy.next