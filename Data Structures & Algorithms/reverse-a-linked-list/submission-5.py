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
            else:
                return head

        def iter(head):
            if not head:
                return None
            
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
                

            return prev


            
        
        return iter(head)


'''
2 -> 1 -> None
1 -> 2 - > 3 -> 4

            temp = 4
            3 <- 4
        temp = 4 -> 3
        2 <- 3
    temp = 4 -> 3 -> 2




'''