# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# n -> b -> c -> none

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        prev = None

        while head:

            node = head
            head = head.next

            node.next = prev

            prev = node

        
        return prev
        