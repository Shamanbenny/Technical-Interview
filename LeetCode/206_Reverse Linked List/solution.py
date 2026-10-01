# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        one, two = None, head
        while two:
            three = two.next
            two.next = one
            one = two
            two = three
        return one
