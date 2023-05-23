class listNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None

    def push(self, x):
        if (self.head is None):
            self.head = listNode(x)
        else:
            y = listNode(x)
            y.next = self.head # type: ignore
            self.head = y

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def pop(self):
        if self.head is None:
            return None
        else:
           self.head = self.head.next

    def print(self):
        while (self.head):
            print(self.head.data)
            self.head = self.head.next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.print()
