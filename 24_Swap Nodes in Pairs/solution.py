# Solution Info (Mathematical Induction Solving Method):
# Runtime: 30 ms, faster than 87.53% of Python3 submissions.
# Memory: 16.25 MB, less than 99.69% of Python3 submissions.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge Case Check (where length == 0 or length == 1)
        if (head == None) or (head.next == None):
            return head

        # Adjust first 2 nodes (Basis Step)
        prev, left, right = None, head, head.next
        head = right
        left.next = right.next
        head.next = left

        print(head.val, head.next.val, head.next.next.val)
        # Induction Step
        prev = left
        while (prev.next != None) and (prev.next.next != None):
            # Sets Left and Right relative to Prev
            left = prev.next
            right = left.next

            # Swap the Nodes
            prev.next = right
            left.next = right.next
            right.next = left

            # Advance the loop via Prev
            prev = left

        return head
