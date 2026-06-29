"""Bài 7: Đảo ngược hàng đợi
"""
from btap16 import QueueArray


def reverse_queue(q: QueueArray):
    # use stack
    stack = []
    while not q.isEmpty():
        stack.append(q.dequeue())
    while stack:
        q.enqueue(stack.pop())

if __name__ == '__main__':
    q = QueueArray(10)
    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    reverse_queue(q)
    print(q.dequeue(), q.dequeue(), q.dequeue())  # 3 2 1
