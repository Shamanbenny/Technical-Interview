## `TreeNode` Class
```
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def visit(node):
    print(node.value, end=" ")
```

## In-Order Traversal
```
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.right)
```

## Pre-Order Traversal
```
def pre_order_traversal(node):
    if node:
        visit(node)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
```

## Post-Order Traversal
```
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        visit(node)
```

## Level-Order Traversal [Uses Queue]
```
from collections import deque

def level_order_traversal(root):
    if root:
        queue = deque()
        queue.append(root)

        while queue:
            current = queue.popleft()       # Dequeue the front node
            visit(current)                  # Visit the node

            if current.left:
                queue.append(current.left)  # Enqueue left child
            if current.right:
                queue.append(current.right) # Enqueue right child
```