"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks. 
"""
class MyQueue:
    def __init__(self):
        self.stack_in, self.stack_out = [], []

    def size(self) -> int:
        return len(self.stack_in) + len(self.stack_out)
    
    def is_empty(self) -> bool:
        return self.size() == 0
    
    def enqueue(self, value: int):
        self.stack_in.append(value)

    def shiftStack(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) != 0:
                self.stack_out.append(self.stack_in.pop())
    
    def peek(self):
        if self.is_empty():
            return None
        self.shiftStack()
        return self.stack_out[-1]
    
    def dequeue(self):
        if self.is_empty():
            return None
        self.shiftStack()
        return self.stack_out.pop()
    
    def print(self):
        buffer = []
        for item in self.stack_out[::-1]:
            buffer.append(str(item) + ",")
        for item in self.stack_in:
            buffer.append(str(item) + ",")
        output = "".join(buffer)
        if len(output) == 0:
            print("[]")
        else:
            print("[" + output[:-1:] + "]")
    
queue = MyQueue()

# Test 1: Enqueue elements and check peek
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
assert queue.peek() == 1, "Test 1.1 Failed"

# Test 2: Dequeue elements and check order
assert queue.dequeue() == 1, "Test 2.1 Failed"
assert queue.dequeue() == 2, "Test 2.2 Failed"

# Test 3: Check is_empty after some dequeues
assert not queue.is_empty(), "Test 3.1 Failed"

# Test 4: Dequeue remaining element
assert queue.dequeue() == 3, "Test 4.1 Failed"

# Test 5: Check is_empty when queue is empty
assert queue.is_empty(), "Test 5.1 Failed"

# Test 7: Interleaved operations
queue.enqueue(10)
queue.enqueue(20)
assert queue.dequeue() == 10, "Test 7.1 Failed"
queue.enqueue(30)
assert queue.dequeue() == 20, "Test 7.2 Failed"
assert queue.dequeue() == 30, "Test 7.3 Failed"
assert queue.is_empty(), "Test 7.4 Failed"

# Test 8: Printing
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
assert queue.peek() == 10, "Test 8.1 Failed"
queue.enqueue(40)
queue.enqueue(50)
queue.print() # Expected: [10,20,30,40,50]
assert queue.dequeue() == 10, "Test 8.2 Failed"
queue.print() # Expected: [20,30,40,50]

print("All test cases passed!")