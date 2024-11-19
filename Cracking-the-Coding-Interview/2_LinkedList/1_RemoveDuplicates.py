from LinkedList import LinkedList
"""
Remove Dups: Write code to remove duplicates from an unsorted linked list. 

FOLLOW UP 
How would you solve this problem if a temporary buffer is not allowed?
"""
def removeDups(list: LinkedList):
    # Temporary Buffer method
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    seen = []
    prev = None
    curr = list.head
    while (curr):
        if curr.value in seen:
            prev.next = curr.next
            curr = curr.next
        else:
            seen.append(curr.value)
            prev = curr
            curr = curr.next

def removeDups_followUp(list: LinkedList):
    # No Temporary Buffer method
    # Time Complexity: O(N^2)
    # Space Complexity: O(1)
    curr = list.head
    while (curr):
        runner = curr
        while (runner.next):
            if (curr.value == runner.next.value):
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next

test_list = LinkedList([3,2,1,3,5,6,2,6,3,1])
removeDups(test_list)
print("Temporary Buffer method: \t" + str(test_list.display()))

test_list = LinkedList([3,2,1,3,5,6,2,6,3,1])
removeDups_followUp(test_list)
print("No Temporary Buffer method: \t" + str(test_list.display()))