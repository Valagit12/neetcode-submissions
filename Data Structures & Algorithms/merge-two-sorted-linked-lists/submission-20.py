# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        

        startnode = ListNode(0, None)
        headans = startnode
        while list1 and list2:
            if list1.val > list2.val:
                headans.next = list2
                list2 = list2.next
            else:
                headans.next = list1
                list1 = list1.next
            
            headans = headans.next

        if not list1 and list2:
            headans.next = list2
        if not list2 and list1:
            headans.next = list1
        
        return startnode.next