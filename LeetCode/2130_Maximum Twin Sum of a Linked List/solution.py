# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        maxSum = float("-inf")
        curr = head
        while prev:
            maxSum = max(maxSum, curr.val + prev.val)
            curr = curr.next
            prev = prev.next
        return maxSum
