#include <stack>

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1;
        stack<int> s2;
        while (l1->next) {
            s1.push(l1->val);
            l1 = l1->next;
        }
        s1.push(l1->val);
        while (l2->next) {
            s2.push(l2->val);
            l2 = l2->next;
        }
        s2.push(l2->val);

        ListNode* result_head = nullptr;
        int carry = 0;
        while (!s1.empty() || !s2.empty() || carry != 0) {
            int sum = carry;
            if (!s1.empty()) {
                sum += s1.top();
                s1.pop();
            }
            if (!s2.empty()) {
                sum += s2.top();
                s2.pop();
            }
            carry = sum / 10;
            result_head = new ListNode(sum % 10, result_head);
        }
        return result_head;
    }
};
