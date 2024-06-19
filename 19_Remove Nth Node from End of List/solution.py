# Solution Info (One Pass solution using buffers)
# Runtime: 30 ms, faster than 91.45% of Python3 submissions.
# Memory: 16.38 MB, less than 97.00% of Python3 submissions.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def removeTail(head: Optional[ListNode]):
            prevNode = None
            currNode = head
            while currNode.next != None:
                prevNode = currNode
                currNode = currNode.next
            if prevNode == None:
                return None
            else:
                prevNode.next = None
                return head

        if n == 1:
            # Edge Case when n == 1
            return removeTail(head)

        currNode = head
        buffer = head
        bufferCount = 0

        while currNode.next != None:
            if bufferCount >= n:
                buffer = buffer.next
            bufferCount += 1
            currNode = currNode.next

        if bufferCount + 1 == n:
            # Edge Case when n == sz
            head = head.next
        else:
            buffer.next = buffer.next.next
        return head
