"""Bài 3: Mô phỏng dãy thao tác enqueue/dequeue
"""

def simulate_queue(ops):
    from btap16 import QueueArray
    q = QueueArray(100)
    outputs = []
    for op in ops:
        if op[0] == 'enqueue':
            q.enqueue(op[1])
        elif op[0] == 'dequeue':
            try:
                outputs.append(q.dequeue())
            except IndexError:
                outputs.append('underflow')
    return outputs

if __name__ == '__main__':
    print(simulate_queue([('enqueue',5),('enqueue',7),('dequeue',None)]))
