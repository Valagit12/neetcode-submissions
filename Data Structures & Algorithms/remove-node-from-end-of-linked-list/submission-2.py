# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        prev = None
        while right:
            right = right.next
            prev = left
            left = left.next
        
        if prev:
            prev.next = left.next
        else:
            return head.next

        return head

        

        

        