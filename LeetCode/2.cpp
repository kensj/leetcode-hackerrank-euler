/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = 0;
        int carry = 0;
        
        ListNode resultNode(0);
        ListNode* resultHead = &resultNode;
        ListNode* resultPointer = &resultNode;
        
        while(l1 != NULL || l2 != NULL || carry) {
            sum = carry;
            if(l1!=NULL) sum += l1->val;
            if(l2!=NULL) sum += l2->val;
            if(sum >= 10) {
                carry = 1;
                sum = sum % 10;
            }
            else carry = 0;
            resultPointer->next = new ListNode(sum);
            resultPointer = resultPointer->next;
            if(l1 && l1->next) l1 = l1->next;
            else l1 = NULL;
            if(l2 && l2->next) l2 = l2->next;       
            else l2 = NULL;
        }
        return resultHead->next;
    }
};