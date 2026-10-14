# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        fast = head.next
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        first, second = head, slow.next
        slow.next = None
        
        prev = None
        while second:
            nextelem = second.next
            second.next = prev
            prev = second
            second = nextelem

        '''
        3 -> 2 ->1 -> 8.  5.       1 -> 5

        2 -> 8 
        '''

        while first and prev:
            nexthead = first.next
            nextprev = prev.next

            first.next = prev
            prev.next = nexthead
            
            first = nexthead
            prev = nextprev
        

            