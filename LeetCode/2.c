/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode  retNode;
    struct ListNode* newNode = &retNode;
    int ret = 0;
    while (l1 || l2 || ret) {
        if (l1) {
            ret += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            ret += l2->val;
            l2 = l2->next;
        }
        newNode = newNode->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = ret % 10;
        ret /= 10;
    }
    newNode->next = NULL;
    return retNode.next;
}
