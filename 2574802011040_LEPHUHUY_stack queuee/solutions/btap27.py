"""Bài 12 (thay số): Josephus - using queue simulation
"""
from collections import deque

def josephus(n, k):
    q = deque(range(1, n+1))
    while len(q) > 1:
        q.rotate(- (k-1))
        q.popleft()
    return q[0]

if __name__ == '__main__':
    print(josephus(5,2))  # 3
