# Solution Info (Naive Head Lookup Approach):
# Runtime: 2209 ms, faster than 9.93% of Python3 submissions.
# Memory: 19.19 MB, less than 96.52% of Python3 submissions.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None

        resultsHead, currResult = None, None
        minIdx = -2
        while minIdx != -1:
            minVal = 20000
            minIdx = -1
            for idx, each in enumerate(lists):
                if each != None:
                    if each.val < minVal:
                        minVal = each.val
                        minIdx = idx
                        if (currResult != None) and (each.val == currResult.val):
                            break
            if minIdx != -1:
                if resultsHead == None:
                    resultsHead = ListNode(minVal, None)
                    currResult = resultsHead
                else:
                    currResult.next = ListNode(minVal, None)
                    currResult = currResult.next
                lists[minIdx] = lists[minIdx].next
                while (
                    (minIdx != -2)
                    and (lists[minIdx] != None)
                    and (currResult.val == lists[minIdx].val)
                ):
                    currResult.next = ListNode(minVal, None)
                    currResult = currResult.next
                    lists[minIdx] = lists[minIdx].next
        return resultsHead


# Total Time Complexity: O(n * k)
# Where n is the number of lists and k is the average length of the lists.
# Therefore, in the worse case scenario, the time complexity is O(n^2).

# The reason for high runtime is due to the need to traverse the entire lists to find the Minimum Value.
# Which in itself takes O(n) time.
# Therefore, to optimise the solution, we can use a MinHeap to store the first element of each list.
# Which will reduce the time complexity to O(log n) instead!
