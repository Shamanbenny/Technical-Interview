# Python List Operations for Stack and Queue

Python's `list` data structure can be used to mimic stack and queue operations such as `insertHead`, `insertTail`, `popHead`, and `popTail`. Below is a detailed explanation of these operations and their equivalents in Python.

## Imports Required
```
from collections import deque

my_deque = deque([1, 2, 3])
```

## Operations and their Equivalents:
1. `insertHead`
- Description: Inserts an element at the start of the list.
- Python Equivalent: ```my_deque.appendleft(value)```

2. `insertTail`
- Description: Appends an element at the end of the list.
- Python Equivalent: ```my_deque.append(value)```

3. `popHead`
- Removes and returns the first element of the list.
- Python Equivalent: ```my_deque.popleft()```

4. `popTail`
- Removes and returns the last element of the list.
- Python Equivalent: ```my_deque.pop()```

## Time Complexity
We avoid using Python's Lists and perform `list.insert(0, value)` or `list.pop(0)`, as it's Time Complexity for either operations are O(n).
Instead, using Python's Deque to perform `my_deque.appendleft(value)` or `my_deque.popleft()` has a Time Complexity for either operations as O(1).