"""Bài 10: Cài đặt ngăn xếp bằng hai hàng đợi
Ở đây push O(1), pop O(n)
"""

from collections import deque

class StackWithQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            raise IndexError('underflow')
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return val

if __name__ == '__main__':
    s = StackWithQueues()
    s.push(1); s.push(2); s.push(3)
    print(s.pop())  # 3
