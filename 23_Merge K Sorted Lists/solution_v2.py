# Solution Info (Heap Approach):
# Runtime: 71 ms, faster than 85.88% of Python3 submissions.
# Memory: 19.71 MB, less than 41.54% of Python3 submissions.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None

        resultsHead, currResult = None, None
        minHeap = []
        for idx, each in enumerate(lists):
            if each != None:
                heapq.heappush(minHeap, (each.val, idx))

        while minHeap != []:
            minVal, idx = heapq.heappop(minHeap)
            if resultsHead == None:
                resultsHead = ListNode(minVal, None)
                currResult = resultsHead
            else:
                currResult.next = ListNode(minVal, None)
                currResult = currResult.next
            lists[idx] = lists[idx].next
            while (
                (idx != -2)
                and (lists[idx] != None)
                and (currResult.val == lists[idx].val)
            ):
                currResult.next = ListNode(minVal, None)
                currResult = currResult.next
                lists[idx] = lists[idx].next
            if lists[idx] != None:
                heapq.heappush(minHeap, (lists[idx].val, idx))
        return resultsHead


# Total Time Complexity: O(n log n)
