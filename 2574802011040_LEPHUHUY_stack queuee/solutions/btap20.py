"""Bài 5: Tìm front và rear
"""
from btap16 import QueueArray

if __name__ == '__main__':
    q = QueueArray(5)
    q.enqueue(4); q.enqueue(5); q.enqueue(6)
    print('front=', q.front())
    print('rear=', q.data[(q.front_idx+q.size-1)%q.capacity])
