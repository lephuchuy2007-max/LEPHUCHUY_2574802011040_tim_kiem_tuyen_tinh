"""Bài 2: Hàng đợi vòng (Circular Queue)
"""

class CircularQueue:
    def __init__(self, capacity):
        self.cap = capacity
        self.data = [None]*capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.cap

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError('full')
        self.data[self.rear] = x
        self.rear = (self.rear + 1) % self.cap
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('underflow')
        val = self.data[self.front]
        self.front = (self.front + 1) % self.cap
        self.count -= 1
        return val


if __name__ == '__main__':
    q = CircularQueue(4)
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    print(q.dequeue())
