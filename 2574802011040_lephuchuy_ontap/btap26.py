class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            raise IndexError('Queue is full')
        self.data[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError('Queue is empty')
        x = self.data[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return x

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    q = CircularQueue(5)
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.dequeue())
