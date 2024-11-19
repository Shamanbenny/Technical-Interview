from LinkedList import LinkedList
"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""
def checkPalindrome(llist: LinkedList) -> bool:
    firstHalf = LinkedList([])
    curr = llist.head
    fast = llist.head
    isOdd = False
    while (fast and fast.next):
        fast = fast.next.next
        firstHalf.prepend(curr.value)
        curr = curr.next
    if fast:
        isOdd = True
    fast = firstHalf.head   # Recycling pointer
    while (fast and curr):
        if fast.value != curr.value:
            if isOdd and fast == firstHalf.head:
                curr = curr.next
                continue
            return False
        fast = fast.next
        curr = curr.next
    return True
    
llist = LinkedList([0,1,2,1,0])
print("Odd Linked List: " + str(checkPalindrome(llist)))

llist = LinkedList([0,1,1,0])
print("Even Linked List: " + str(checkPalindrome(llist)))

llist = LinkedList([0,1,2,0])
print("Even Linked List: " + str(checkPalindrome(llist)))

llist = LinkedList([0,1,1,2])
print("Even Linked List: " + str(checkPalindrome(llist)))

llist = LinkedList([0,1,3,1,2])
print("Odd Linked List: " + str(checkPalindrome(llist)))

llist = LinkedList([0,1,1,1,2])
print("Odd Linked List: " + str(checkPalindrome(llist)))

llist = LinkedList([1])
print("Odd Linked List: " + str(checkPalindrome(llist)))

llist = LinkedList([1, 1])
print("Even Linked List: " + str(checkPalindrome(llist)))

llist = LinkedList([1, 0])
print("Even Linked List: " + str(checkPalindrome(llist)))