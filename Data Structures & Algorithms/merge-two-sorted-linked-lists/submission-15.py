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
        def recursive(list1, list2):
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            
            nextinl1 = list1.next
            nextinl2 = list2.next
            if list1.val <= list2.val:
                list2 = recursive(nextinl1,list2)
                list1.next = list2
                return list1
            else:
                list1 = recursive(list1, nextinl2)
                list2.next = list1
                ans = list2
                while list2:
                    print(list2.val, end = ' ')
                    list2 = list2.next
                print()
                return ans
        

        def iterative(list1, list2):
            '''
                head = 3
                1 ->1 2 -> 4
                      ^     
                1 -> 3 -> 5
                     ^

                5
                ^
                1 -> 5 3 -> 4
                       ^
                
                                     
            '''
            if not list1:
                return list2
            if not list2:
                return list1
            
            head = list1 if list1.val <= list2.val else list2

            prev = None
            
            while list1 and list2:
                
                if list1.val <= list2.val:
                    if prev: prev.next = list1
                    prev = list1
                    list1 = list1.next
                else:
                    if prev: prev.next = list2
                    prev = list2
                    list2 = list2.next

            if not list1 and list2:
                prev.next = list2
            if not list2 and list1:
                prev.next = list1

            
            return head
            

        

        return iterative(list1, list2)

        
        

            
                    


        