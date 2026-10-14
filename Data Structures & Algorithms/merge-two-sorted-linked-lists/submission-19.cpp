/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
    /**
        1 -> 2 -> 4
        1 -> 3 -> 5


    */
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // if (!list1) return list2;
        // if (!list2) return list1;

        // if (list1->val < list2->val) {
        //     ListNode *nextl1 = list1->next;
        //     list1->next = mergeTwoLists(nextl1, list2);
        //     return list1;
        // } else {
        //     ListNode *nextl2 = list2->next;
        //     list2->next = mergeTwoLists(list1, nextl2);
        //     return list2;
        // }

        ListNode* dummy;
        ListNode* ans = dummy;

        if (!list1) return list2;
        if (!list2) return list1;

        while (list1 && list2) {
            if (list1->val <= list2->val) {
                dummy->next = list1;
                list1 = list1->next;
            } else {
                dummy->next = list2;
                list2 = list2->next;
            }
            dummy = dummy->next;
        }

        if (!list1) dummy->next = list2;
        if (!list2) dummy->next = list1;
        
        return ans->next;
    }
};
