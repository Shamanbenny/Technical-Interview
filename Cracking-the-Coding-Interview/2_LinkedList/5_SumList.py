from LinkedList import LinkedList, Node
"""
Sum Lists: You have two numbers represented by a linked list, where each node contains a single 
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a 
function that adds the two numbers and returns the sum as a linked list. 

EXAMPLE 
Input: (7->1->6) + (5->9->2). That is 617 + 295
Output: (2->1->9). That is 912.

FOLLOW UP 
Suppose the digits are stored in forward order. Repeat the above problem. 
Input: (6->1->7) + (2->9->5). That is 617 + 295
Output: (9->1->2). That is 912.
"""
def getSum(n1: int, n2: int):
    sum = n1 + n2
    if sum >= 10:
        return (1, sum - 10)
    return (0, sum)

def sumList(l1: LinkedList, l2: LinkedList) -> LinkedList:
    # Assume Reverse Order of Linked List
    result = LinkedList([])
    _sumList(l1.head, l2.head, 0, result)
    return result

def _sumList(n1: Node, n2: Node, carry: int, result: LinkedList):
    if n1 and n2:
        tmp = getSum(n1.value, n2.value + carry)
        carry = tmp[0]
        result.append(tmp[1])
        _sumList(n1.next, n2.next, carry, result)
    elif n1:
        tmp = getSum(n1.value, carry)
        carry = tmp[0]
        result.append(tmp[1])
        _sumList(n1.next, None, carry, result)
    elif n2:
        tmp = getSum(n2.value, carry)
        carry = tmp[0]
        result.append(tmp[1])
        _sumList(None, n2.next, carry, result)
    else:
        return
    
def sumList_forward(l1: LinkedList, l2: LinkedList) -> LinkedList:
    # Assume Forward Order of Linked List [FOLLOW UP]
    result = LinkedList([])
    _sumList_forward(l1.head, l2.head, result)
    return result

def _sumList_forward(n1: Node, n2: Node, result: LinkedList) -> int:
    if n1 and n2:
        carry = _sumList_forward(n1.next, n2.next, result)
        tmp = getSum(n1.value, n2.value + carry)
        result.prepend(tmp[1])
        return tmp[0]
    elif n1:
        carry = _sumList_forward(n1.next, None, result)
        tmp = getSum(n1.value, carry)
        result.prepend(tmp[1])
        return tmp[0]
    elif n2:
        carry = _sumList_forward(None, n2.next, result)
        tmp = getSum(n2.value, carry)
        result.prepend(tmp[1])
        return tmp[0]
    else:
        return 0
    
l1 = LinkedList([7,1,6])
l2 = LinkedList([5,9,2])
print("Reversed Sum List: " + str(sumList(l1, l2).display()))

l1 = LinkedList([6,1,7])
l2 = LinkedList([2,9,5])
print("Forward Sum List: " + str(sumList_forward(l1, l2).display()))