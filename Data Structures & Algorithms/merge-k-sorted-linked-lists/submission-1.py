# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1

            head = l1 if l1.val <= l2.val else l2
            prev = None
            while l1 and l2:
                if l1.val <= l2.val:
                    if prev: prev.next = l1
                    prev = l1
                    l1 = l1.next
                else:
                    if prev: prev.next = l2
                    prev = l2
                    l2 = l2.next
                
            if not l1: prev.next = l2
            if not l2: prev.next = l1
            
            
            return head
        


        if not lists:
            return None
        for i, l in enumerate(lists):
            if l:
                break
            elif i == len(lists) - 1:
                return None
        
        n = len(lists)

        if n == 1:
            return lists[0]
        if n == 2:
            return merge(lists[0], lists[1])

        mid = n // 2

        l1 = self.mergeKLists(lists[0:mid])
        l2 = self.mergeKLists(lists[mid:])

        
        
        

            

        return merge(l1, l2)
            

        

        
            

            


        