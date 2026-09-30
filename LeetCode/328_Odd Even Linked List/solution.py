# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        evenHead, curr, odd, even = head.next, head.next.next, head, head.next
        isOdd = True
        while curr:
            if isOdd:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            if curr.next:
                curr = curr.next
            else:
                break
            isOdd = not isOdd
        if isOdd:
            even.next = None
        odd.next = evenHead
        return head

