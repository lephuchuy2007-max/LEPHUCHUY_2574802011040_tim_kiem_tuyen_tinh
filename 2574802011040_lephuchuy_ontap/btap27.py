class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError('Queue is empty')
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            return None
        return self.out_stack[-1]


if __name__ == '__main__':
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
