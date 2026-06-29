"""Bài 6: Hàng đợi bằng hai ngăn xếp
"""

class QueueTwoStacks:
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
            raise IndexError('underflow')
        return self.out_stack.pop()

if __name__ == '__main__':
    q = QueueTwoStacks()
    q.enqueue(1); q.enqueue(2)
    print(q.dequeue())
