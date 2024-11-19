from LinkedList import LinkedList, Node
"""
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the 
beginning of the loop. 
DEFINITION 
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so 
as to make a loop in the linked list. 
EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier] 
Output: C 
"""
# This problem is quite difficult to interpret, probably requires drawing the problem out and analysing it.
# But we do know that a fast and slow pointer is the solution to such a problem.
# [NOTE] When Fast and Slow collide, they should both be k number of Nodes away from start of Loop, where k is
#           the number of node from LinkedListHead to start of Loop.
def loopDetection(llist: LinkedList) -> Node:
    slow = llist.head
    fast = llist.head
    
    while (fast and fast.next):
        fast = fast.next.next
        slow = slow.next
        if (slow == fast):
            break
    if not fast or not fast.next:
        return None
    
    slow = llist.head
    while (slow != fast):
        slow = slow.next
        fast = fast.next
    return slow

llist = LinkedList([39, 96, 82, 45, 94, 70, 80, 4, 99, 63, 91, 46, 69, 86, 94, 63, 49, 82, 61, 98])
startOfLoop = llist.head.next.next.next # 45
curr = llist.head
while curr.next:
    curr = curr.next
curr.next = startOfLoop
print("Start of Loop (Expected: 45): Node w/ value " + str(loopDetection(llist).value))

llist = LinkedList([39, 96, 82, 45, 94, 70, 80, 4, 99, 63, 91, 46, 69, 86, 94, 63, 49, 82, 61, 98])
startOfLoop = llist.head.next.next.next.next.next # 70
curr = llist.head
while curr.next:
    curr = curr.next
curr.next = startOfLoop
print("Start of Loop (Expected: 70): Node w/ value " + str(loopDetection(llist).value))