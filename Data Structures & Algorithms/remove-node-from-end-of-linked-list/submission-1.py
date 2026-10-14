# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            length+=1
            curr = curr.next
        
        number = length - n

        prev = None
        ans = head
        i = 0
        while head:
            if i == number and prev:
                prev.next = head.next
                return ans
            elif i == number and not prev:
                return head.next
                
            prev = head
            head = head.next
            i+=1

        return ans
        

        