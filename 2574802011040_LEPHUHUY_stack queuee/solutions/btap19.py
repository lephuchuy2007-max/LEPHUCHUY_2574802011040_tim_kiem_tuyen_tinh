"""Bài 4: Kiểm tra rỗng / đầy cho hàng đợi (đã có trong btap16)
"""

from btap16 import QueueArray

if __name__ == '__main__':
    q = QueueArray(2)
    q.enqueue(1); q.enqueue(2)
    try:
        q.enqueue(3)
    except OverflowError:
        print('overflow')
    q.dequeue(); q.dequeue()
    try:
        q.dequeue()
    except IndexError:
        print('underflow')
