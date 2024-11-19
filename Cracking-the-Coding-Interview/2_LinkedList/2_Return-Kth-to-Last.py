from LinkedList import LinkedList, Node
"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

E.g. If k = 2, return the 2nd last element of the Linked List.

We're going to assume the size of Linked List is NOT known beforehand.
(LinkedList does not have _size...)
"""
# Using Recursive method to achieve O(N) Time Complexity
# [NOTE] Whenever you wish to have a doubly linked LinkedList, you can do said iteration using Recursive Stack Calls
def k_toLast(llist: LinkedList, k: int):
    head = llist.head
    if head:
        return recursive(head, k)[0]
    return None

def recursive(node: Node, k: int):
    if (node.next):
        result = recursive(node.next, k)
        if result[0]:
            return result
        if k == result[1] + 1:
            return (node.value, result[1] + 1)
        return (None, result[1] + 1)
    else:
        if k == 1:
            return (node.value, 1)
        return (None, 1)
    
# Using Iterative method to ALSO achieve O(N) Time Complexity
# [NOTE] Not as ituitive an approach, but easier to implement once you understood
def k_toLast_iter(llist: LinkedList, k: int):
    curr = llist.head
    delayed = llist.head
    for _ in range(k):
        if not curr:
            return None
        curr = curr.next

    while (curr):
        curr = curr.next
        delayed = delayed.next
    
    return delayed.value
    
llist = LinkedList([39, 96, 82, 45, 94, 70, 80, 4, 99, 63, 91, 46, 69, 86, 94, 63, 49, 82, 61, 98])
print("2nd Last Element: " + str(k_toLast(llist, 2)))
print("3rd Last Element: " + str(k_toLast(llist, 3)))
print("10th Last Element: " + str(k_toLast(llist, 10)))

print("2nd Last Element (ITERATIVE): " + str(k_toLast_iter(llist, 2)))
print("3rd Last Element (ITERATIVE): " + str(k_toLast_iter(llist, 3)))
print("10th Last Element (ITERATIVE): " + str(k_toLast_iter(llist, 10)))