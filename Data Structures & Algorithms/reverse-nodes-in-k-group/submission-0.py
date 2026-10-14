# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def iterreverse(l, k):
            n = k
            if l == None:
                return None

            head = l;
            while k > 0 and head:
                head = head.next
                k -= 1
            if k > 0:
                return l
            
            k = n
            head = l
            prev = None
            while l and k > 0:
                k-=1
                nextl = l.next
                l.next = prev
                prev = l
                l = nextl
            
            head.next = iterreverse(l, n)
            return prev  

        h = iterreverse(head, k)
        return h



        


        