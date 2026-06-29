"""Bài 7: Min Stack — getMin O(1)
"""
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.stack:
            raise IndexError('underflow')
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def getMin(self):
        if not self.min_stack:
            raise IndexError('empty')
        return self.min_stack[-1]

if __name__ == '__main__':
    m = MinStack()
    m.push(5); m.push(3); m.push(7)
    print(m.getMin())  # 3
