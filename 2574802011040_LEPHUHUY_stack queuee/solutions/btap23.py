"""Bài 8: Deque (hàng đợi hai đầu)
"""

class Deque:
    def __init__(self):
        self.data = []

    def pushFront(self, x):
        self.data.insert(0, x)

    def pushBack(self, x):
        self.data.append(x)

    def popFront(self):
        if not self.data:
            raise IndexError('underflow')
        return self.data.pop(0)

    def popBack(self):
        if not self.data:
            raise IndexError('underflow')
        return self.data.pop()

if __name__ == '__main__':
    d = Deque()
    d.pushFront(1); d.pushBack(2)
    print(d.popFront(), d.popBack())
