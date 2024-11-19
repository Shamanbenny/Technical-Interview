from LinkedList import LinkedList
"""
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come 
before all nodes greater than or equal to x. If xis contained within the list the values of x only need 
to be after the elements less than x (see below). The partition element x can appear anywhere in the 
"right partition"; it does not need to appear between the left and right partitions. 

EXAMPLE 
Input: 3->5->8->5->10->2->1 [Partition = 5]
Output: 3->1->2->10->5->5->8
"""
def partition(llist: LinkedList, partition: int):
    smaller = LinkedList([])
    larger = LinkedList([])
    curr = llist.head
    while curr:
        if curr.value < partition:
            smaller.append(curr.value)
        else:
            larger.append(curr.value)
        curr = curr.next
    llist.head = LinkedList(smaller.display() + larger.display()).head

def quickSortPatition(llist: LinkedList, partition: int):
    smaller = LinkedList([])
    larger = LinkedList([])
    count = 0
    curr = llist.head
    while curr:
        if curr.value < partition:
            smaller.append(curr.value)
        elif curr.value == partition:
            count += 1
        else:
            larger.append(curr.value)
        curr = curr.next
    llist.head = LinkedList(smaller.display() + [partition] * count + larger.display()).head

llist = LinkedList([3,5,8,5,10,2,1])
partition(llist, 5)
print("Partition by 5: " + str(llist.display()))

llist = LinkedList([3,5,8,5,10,2,1])
partition(llist, 7)
print("Partition by 7: " + str(llist.display()))

llist = LinkedList([3,5,8,5,10,2,1])
quickSortPatition(llist, 5)
print("Partition by 5 (for QuickSort): " + str(llist.display()))

llist = LinkedList([3,5,8,5,10,2,1])
quickSortPatition(llist, 7)
print("Partition by 7 (for QuickSort): " + str(llist.display()))