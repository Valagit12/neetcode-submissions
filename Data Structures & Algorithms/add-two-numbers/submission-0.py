# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def recurse(l1, l2, carry):

            if not l1 and not l2 and not carry:
                return None
            
            (n1, d1), (n2, d2) = ((l1.next, l1.val) if l1 else (None, 0), (l2.next, l2.val) if l2 else (None, 0))
        
            summ = d1 + d2 + carry

            carry = summ // 10
            summ = summ % 10

            copy = ListNode(summ)
            copy.next = recurse(n1, n2, carry)
            
            return copy


        return recurse(l1, l2,  0)


            
        


