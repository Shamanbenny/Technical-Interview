# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        fast, slow, beforeSlow = head, head, None
        while fast.next:
            fast = fast.next
            if fast.next:
                fast = fast.next
            beforeSlow = slow
            slow = slow.next
        if not beforeSlow and slow == fast:
            return None
        beforeSlow.next = slow.next
        return head
