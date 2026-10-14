# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''

0 -> 1 -> 2 -> 3


0 -> 3 -> 1 -> 2

0 -> 3 -> 1 -> 2


'''



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        rev = None
        curr = head
        n = 0
        while curr:
            n+=1
            rev = ListNode(curr.val, rev)
            curr = curr.next
        '''
        2 4 6 8 10
                 
        10 8 6 4 2
        '''
        
        ans = ListNode()

        for i in range(n//2):
            ans.next = head
            nexthead = head.next
            ans.next.next = rev
            head = nexthead
            rev = rev.next
            ans = ans.next.next
        
        rev.next = None
        if n%2 == 0:
            ans.next = None

            
            

        


        
            
        
        

        