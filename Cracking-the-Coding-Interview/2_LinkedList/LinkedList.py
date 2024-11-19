class Node:
    """
    A class representing a single node in a linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list.
    """
    def __init__(self, list: list):
        self.head = None
        for item in list:
            if self.head:
                self.append(item)
            else:
                self.head = Node(item)

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        """
        Prepend a new node with the given value to the start of the linked list.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        """
        Display the linked list as a list of values.
        """
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
    