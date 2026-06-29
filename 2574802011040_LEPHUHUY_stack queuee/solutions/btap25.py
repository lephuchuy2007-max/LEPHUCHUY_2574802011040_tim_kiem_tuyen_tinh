"""Bài 10: Hàng đợi ưu tiên cơ bản
Simple implementation using list (inefficient)
"""

class SimplePriorityQueue:
    def __init__(self, reverse=False):
        self.data = []
        self.reverse = reverse

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if not self.data:
            raise IndexError('empty')
        idx = 0
        for i in range(1, len(self.data)):
            if (not self.reverse and self.data[i] > self.data[idx]) or (self.reverse and self.data[i] < self.data[idx]):
                idx = i
        return self.data.pop(idx)

if __name__ == '__main__':
    pq = SimplePriorityQueue()
    pq.push(3); pq.push(1); pq.push(2)
    print(pq.pop())
