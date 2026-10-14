# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printList(node):
            while node:
                print(node.val, end=", ")
                node = node.next
            print()
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        node = slow.next
        slow.next = None
        prev = None


        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        head2 = prev


        while head and head2:
            temp1 = head.next  
            temp2 = head2.next 
            # 1 -> 2 -> 3
            # 4 -> 5 -> 6
            head.next = head2 
            head2.next = temp1

            head = temp1  
            head2 = temp2 
