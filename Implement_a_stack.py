class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def max(self):
        sort = sorted(self.stack)
        return print(sort.pop())

    def printstack(self):
        for i in self.stack:
            print(i)
            
Value = Stack()
Value.push(10)
Value.push(2)
Value.push(8)
Value.push(5)
Value.printstack()
Value.pop()
Value.printstack()
Value.max()
Value.printstack()
