# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        def recursive(lists):
            if not lists:
                return None
            # base case
            for i,l in enumerate(lists):
                if l:
                    break              
                if i == len(lists) - 1:
                    return None  
            
            minnodeidx = None
            curmin = float('inf')
            for i in range(len(lists)):
                l = lists[i]
                if l:
                    (curmin, minnodeidx) = (l.val, i) if l.val < curmin else (curmin, minnodeidx)
            
            curr = ListNode(lists[minnodeidx].val)
            lists[minnodeidx] = lists[minnodeidx].next

            curr.next = recursive(lists)

            return curr
        
        return recursive(lists)
            
            


        