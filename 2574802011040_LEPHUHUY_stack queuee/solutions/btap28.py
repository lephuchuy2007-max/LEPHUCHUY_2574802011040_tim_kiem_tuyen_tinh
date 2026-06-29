"""Bài 13: Hàng đợi amortized O(1) từ hai ngăn xếp (analysis + demo)
Demonstration already in btap21; here we return amortized explanation as comment.
"""

# Each element is moved at most once from in_stack to out_stack, so total moves O(n) for n ops.

if __name__ == '__main__':
    from btap21 import QueueTwoStacks
    q = QueueTwoStacks()
    for i in range(10): q.enqueue(i)
    for i in range(10): q.dequeue()
    print('done')
