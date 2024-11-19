# Solution Info (Head Pointer Comparison Approach):
# Runtime: 30 ms, faster than 94.53% of Python3 submissions.
# Memory: 16.40 MB, less than 98.19% of Python3 submissions.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        resultHead = None
        currResult = None

        def llistAddTail(val: int):
            nonlocal resultHead, currResult
            if resultHead == None:
                resultHead = ListNode(val, None)
                currResult = resultHead
            else:
                currResult.next = ListNode(val, None)
                currResult = currResult.next

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    llistAddTail(list1.val)
                    list1 = list1.next
                else:
                    llistAddTail(list2.val)
                    list2 = list2.next
            if list1 and not list2:
                llistAddTail(list1.val)
                list1 = list1.next
            if list2 and not list1:
                llistAddTail(list2.val)
                list2 = list2.next

        return resultHead
