"""PHẦN B — HÀNG ĐỢI
Bài 1: Cài đặt hàng đợi cơ bản
"""

class QueueArray:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None]*capacity
        self.front_idx = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self, x):
        if self.isFull():
            raise OverflowError('Queue overflow')
        self.data[(self.front_idx + self.size) % self.capacity] = x
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('underflow')
        val = self.data[self.front_idx]
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.size -= 1
        return val

    def front(self):
        if self.isEmpty():
            raise IndexError('empty')
        return self.data[self.front_idx]


if __name__ == '__main__':
    q = QueueArray(4)
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    print(q.dequeue())  # 1
    print(q.front())
