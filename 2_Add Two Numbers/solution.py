# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Basis Step
        carry = 0
        tmpSum = l1.val + l2.val
        l3_head = ListNode(tmpSum % 10)
        carry = tmpSum // 10
        curr_list = l3_head
        # Induction Step
        while (l1.next != None) or (l2.next != None):
            tmpSum = 0
            if l1.next:
                tmpSum += l1.next.val
                l1 = l1.next
            if l2.next:
                tmpSum += l2.next.val
                l2 = l2.next
            tmpSum += carry
            curr_list.next = ListNode(tmpSum % 10)
            carry = tmpSum // 10
            curr_list = curr_list.next
        if carry == 1:
            curr_list.next = ListNode(1)
        return l3_head
