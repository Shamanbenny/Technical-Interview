from LinkedList import LinkedList, Node
"""
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the 
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the 
kth node of the first linked list is the exact same node (by reference) as the jth node of the second 
linked list, then they are intersecting
"""
# Method 1: Use HashTable on ALL nodes
def intersection_hash(l1: LinkedList, l2: LinkedList) -> Node:
    seen = []
    curr = l1.head
    while curr:
        seen.append(curr)
        curr = curr.next
    curr = l2.head
    while curr:
        if curr in seen:
            return curr
        curr = curr.next
    return None

# Method 2: When Intersection occurs, the tail end of both List is the same.
def intersection(l1: LinkedList, l2: LinkedList) -> Node:
    sizeAndTail1 = _getSizeAndTail(l1)
    sizeAndTail2 = _getSizeAndTail(l2)

    if sizeAndTail1[1] != sizeAndTail2[1]:
        return None
    
    if (sizeAndTail1[0] < sizeAndTail2[0]):
        l1, l2 = l2, l1
        sizeAndTail1, sizeAndTail2 = sizeAndTail2, sizeAndTail1
    
    curr1 = l1.head
    curr2 = l2.head
    for _ in range(sizeAndTail1[0] - sizeAndTail2[0]):
        curr1 = curr1.next

    while (curr1 and curr2):
        if (curr1 == curr2):
            return curr1
        curr1 = curr1.next
        curr2 = curr2.next

def _getSizeAndTail(llist: LinkedList):
    size = 1
    curr = llist.head
    if not curr:
        return (0, None)
    while curr.next:
        size += 1
        curr = curr.next
    return (size, curr)

l1 = LinkedList([1,2])
l2 = LinkedList([3,7,6,5,4])
curr1 = l1.head.next
curr2 = l2.head.next
curr1.next = curr2

print("[ HASHTABLE METHOD ]")
print("No Intersection: " + str(intersection_hash(LinkedList([3,4,5,6,7,8]), LinkedList([1,2,3]))))

print("l1: " + str(l1.display()))
print("l2: " + str(l2.display()))
print("Have intersection: " + str(intersection_hash(l1, l2).value))

print("\n[ SAME TAIL METHOD ]")
print("No Intersection: " + str(intersection(LinkedList([3,4,5,6,7,8]), LinkedList([1,2,3]))))

print("l1: " + str(l1.display()))
print("l2: " + str(l2.display()))
print("Have intersection: " + str(intersection(l1, l2).value))
