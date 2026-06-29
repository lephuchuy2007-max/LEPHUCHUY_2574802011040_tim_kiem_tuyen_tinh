"""Bài 14: Trung bình trượt / đếm hit trong cửa sổ thời gian
Simple hit counter using deque of (timestamp)
"""
from collections import deque

class HitCounter:
    def __init__(self, window):
        self.window = window
        self.q = deque()

    def hit(self, t):
        self.q.append(t)
        while self.q and self.q[0] < t - self.window:
            self.q.popleft()

    def count(self, t):
        while self.q and self.q[0] < t - self.window:
            self.q.popleft()
        return len(self.q)

if __name__ == '__main__':
    hc = HitCounter(300)
    hc.hit(1); hc.hit(100); hc.hit(301)
    print(hc.count(301))
