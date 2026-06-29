"""Bài 1: Cài đặt ngăn xếp bằng mảng (StackArray)
- push, pop, top, isEmpty
- ví dụ: push 1,2,3 rồi pop -> trả về 3
"""

class StackArray:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top_index = -1

    def isEmpty(self):
        return self.top_index == -1

    def isFull(self):
        return self.top_index + 1 == self.capacity

    def push(self, x):
        if self.isFull():
            raise OverflowError("Stack overflow")
        self.top_index += 1
        self.data[self.top_index] = x

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack underflow")
        val = self.data[self.top_index]
        self.top_index -= 1
        return val

    def top(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.data[self.top_index]


if __name__ == '__main__':
    s = StackArray(10)
    s.push(1)
    s.push(2)
    s.push(3)
    print("pop:", s.pop())  # 3
    print("top:", s.top())  # 2
