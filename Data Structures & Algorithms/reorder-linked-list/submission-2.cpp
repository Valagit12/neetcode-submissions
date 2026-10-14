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
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) return nullptr;

        ListNode* dummy = head;
        if (head->next) {
            dummy = reverseList(head->next);
            head->next->next = head;
            head->next = nullptr;
        }
        return dummy;
    }
    // 0 1 2 3 4 5 6 -> null


    void reorderList(ListNode* head) {
        if (!head) return;

        ListNode* fast = head->next;
        ListNode* halfway = head;

        while (fast && fast->next) {
            halfway = halfway->next;
            fast = fast->next->next;
        }

        ListNode* reversed_half = reverseList(halfway->next);
        halfway->next = nullptr;
        ListNode* curr = head;

        while (curr && reversed_half) {
            ListNode* currnext = curr->next;
            ListNode* revhalfnext = reversed_half->next;

            curr->next = reversed_half;
            reversed_half->next = currnext;

            curr = currnext;
            reversed_half = revhalfnext;
        }    
    }
};
