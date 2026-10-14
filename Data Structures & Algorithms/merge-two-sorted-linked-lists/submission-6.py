# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1->1->2 4
^
3 5
^


'''



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        nextinl1 = list1.next
        nextinl2 = list2.next
        if list1.val <= list2.val:
            list2 = self.mergeTwoLists(nextinl1,list2)
            list1.next = list2
            return list1
        else:
            list1 = self.mergeTwoLists(list1, nextinl2)
            list2.next = list1
            ans = list2
            while list2:
                print(list2.val, end = ' ')
                list2 = list2.next
            print()
            return ans
        
        

            
                    


        