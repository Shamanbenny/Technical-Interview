"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min 
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
"""
class StackMin:
    """
    A class representing a Stack capable of O(1) min retrieval.

    Each element of self.stack contains (value, min).
    """
    def __init__(self):
        self.stack = []

    def push(self, value: int):
        if len(self.stack) == 0:
            self.stack.append((value, value))
            return
        min = self.stack[-1][1]
        if value < min:
            min = value
        self.stack.append((value, min))

    def pop(self):
        if len(self.stack) == 0:
            return None
        result = self.stack.pop()
        return result[0]
    
    def min(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]
    
    def print(self):
        values = []
        for value, _min in self.stack:
            values.append(value)
        print(values)
    
stack = StackMin()
# Test 1: Push values and check min
stack.push(5)
assert stack.min() == 5, "Test 1.1 Failed"
stack.push(3)
assert stack.min() == 3, "Test 1.2 Failed"
stack.push(7)
assert stack.min() == 3, "Test 1.3 Failed"
stack.push(3)
assert stack.min() == 3, "Test 1.4 Failed"
stack.print() # Expects: [5, 3, 7, 3]
# Test 2: Pop values and check min
stack.pop()  # Pops 3
assert stack.min() == 3, "Test 2.1 Failed"
stack.pop()  # Pops 7
assert stack.min() == 3, "Test 2.2 Failed"
stack.pop()  # Pops 3
assert stack.min() == 5, "Test 2.3 Failed"
stack.print() # Expects: [5]
# Test 4: Push values in decreasing order
stack = StackMin()
stack.push(10)
stack.push(9)
stack.push(8)
stack.push(7)
stack.push(6)
assert stack.min() == 6, "Test 4.1 Failed"
stack.pop()  # Pops 6
assert stack.min() == 7, "Test 4.2 Failed"
stack.pop()  # Pops 7
assert stack.min() == 8, "Test 4.3 Failed"
print("All test cases passed!")