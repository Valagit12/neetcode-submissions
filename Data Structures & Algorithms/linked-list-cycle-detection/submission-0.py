# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        c = 1
        while fast and slow:
            fast = fast.next
            if c % 2 == 0:
                slow = slow.next
            c+=1
            if fast == slow:
                return True
        return False
        