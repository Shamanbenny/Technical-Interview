class ArrayTripleStack:
    """
    A class representing a Triple Stack system using Array
    """
    def __init__(self, size: int):
        self.maxSize = size
        self.size = [0, 0, 0]
        self.array = [None] * size * 3
    
    def isEmpty(self, stackID: int):
        return self.size[stackID] == 0
    
    def isFull(self, stackID: int):
        return self.size[stackID] == self.maxSize
    
    def push(self, stackID: int, value: int) -> bool:
        if not self.isFull(stackID):
            self.array[stackID * self.maxSize + self.size[stackID]] = value
            self.size[stackID] += 1
            return True
        return False
    
    def pop(self, stackID: int) -> int:
        if not self.isEmpty(stackID):
            tmp = self.array[stackID * self.maxSize + self.size[stackID] - 1]
            self.array[stackID * self.maxSize + self.size[stackID] - 1] = None
            self.size[stackID] -= 1
            return tmp
        return None
    
    def print(self):
        print(self.array)
    
stack = ArrayTripleStack(3)
stack.push(0, 1)
stack.push(1, 2)
stack.push(0, 3)
stack.push(2, 4)
stack.print()
print("Popped: " + str(stack.pop(2)))
stack.print()
print("Popped: " + str(stack.pop(0)))
stack.print()
print("Popped: " + str(stack.pop(2)))
stack.print()