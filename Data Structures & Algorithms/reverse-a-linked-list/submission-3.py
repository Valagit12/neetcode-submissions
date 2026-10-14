# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(head):
            if not head:
                return None

            if head.next:
                temp = rec(head.next)
                head.next.next = head
                head.next = None
                return temp
            head.next = None
            return head
            
        
        return rec(head)


'''

1 -> 2 - > 3 -> 4


'''