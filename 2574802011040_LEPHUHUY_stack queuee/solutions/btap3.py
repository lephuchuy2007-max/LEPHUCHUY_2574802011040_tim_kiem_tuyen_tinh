"""Bài 3: Mô phỏng dãy thao tác push/pop
"""
from btap1 import StackArray


def simulate(ops):
    s = StackArray(100)
    outputs = []
    for op in ops:
        if op[0] == 'push':
            s.push(op[1])
        elif op[0] == 'pop':
            try:
                outputs.append(s.pop())
            except IndexError:
                outputs.append('underflow')
    return outputs


if __name__ == '__main__':
    print(simulate([('push',5), ('push',7), ('pop', None)]))  # [7]
