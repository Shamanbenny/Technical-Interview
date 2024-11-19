from LinkedList import LinkedList
"""
Delete Middle Node: Implement an algorithm to delete a node in the middle of a singly linked list.

EXAMPLE 
Input: Linked List a->b->c->d->e->f 
Result: Nothing is returned, but the new linked list looks like a->b->c->e->f 
"""
def deleteMid(llist: LinkedList):
    fast = llist.head
    slow = None
    if not fast:
        return
    while (fast and fast.next):
        fast = fast.next.next
        if not slow:
            slow = llist.head
        else:
            slow = slow.next
    if slow:
        slow.next = slow.next.next
    else:
        llist.head = None

llist = LinkedList(["a", "b", "c", "d", "e", "f"])
deleteMid(llist)
print("Deleting Middle Node (Even): " + str(llist.display()))

llist = LinkedList(["a", "b", "c", "d", "e"])
deleteMid(llist)
print("Deleting Middle Node (Odd): " + str(llist.display()))

print("[ EDGE CASES ]")

llist = LinkedList(["a", "b", "c"])
deleteMid(llist)
print("Deleting Middle Node: " + str(llist.display()))

llist = LinkedList(["a", "b"])
deleteMid(llist)
print("Deleting Middle Node: " + str(llist.display()))

llist = LinkedList(["a"])
deleteMid(llist)
print("Deleting Middle Node: " + str(llist.display()))