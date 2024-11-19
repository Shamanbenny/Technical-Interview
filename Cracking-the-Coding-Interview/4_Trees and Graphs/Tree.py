class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def visit(node):
    print(node.value, end=" ")

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)  # Traverse left subtree
        visit(node)  # Visit the node
        in_order_traversal(node.right)  # Traverse right subtree

def pre_order_traversal(node):
    if node:
        visit(node)  # Visit the node
        pre_order_traversal(node.left)  # Traverse left subtree
        pre_order_traversal(node.right)  # Traverse right subtree

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)  # Traverse left subtree
        post_order_traversal(node.right)  # Traverse right subtree
        visit(node)  # Visit the node

from collections import deque

def level_order_traversal(root):
    if not root:
        return
    
    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()  # Dequeue the front node
        visit(current)  # Visit the node

        if current.left:
            queue.append(current.left)  # Enqueue left child
        if current.right:
            queue.append(current.right)  # Enqueue right child

# Create a binary tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, TreeNode(6), TreeNode(7))

# Test Traversals
print("In-Order Traversal:")
in_order_traversal(root)  # Output: 4 2 5 1 6 3 7
print("\nPre-Order Traversal:")
pre_order_traversal(root)  # Output: 1 2 4 5 3 6 7
print("\nPost-Order Traversal:")
post_order_traversal(root)  # Output: 4 5 2 6 7 3 1
print("\nLevel-Order Traversal:")
level_order_traversal(root)  # Output: 1 2 3 4 5 6 7
print("")
