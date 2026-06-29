"""
Bài 1: ArrayList cơ bản (add/get/set/size)
"""
class ArrayList:
    def __init__(self, capacity=4):
        self._cap = capacity
        self._data = [None] * self._cap
        self._n = 0

    def size(self):
        return self._n

    def _check_index(self, i):
        if i < 0 or i >= self._n:
            raise IndexError('index out of range')

    def add(self, val):
        if self._n == self._cap:
            self._resize(self._cap * 2)
        self._data[self._n] = val
        self._n += 1

    def get(self, i):
        self._check_index(i)
        return self._data[i]

    def set(self, i, val):
        self._check_index(i)
        self._data[i] = val

    def _resize(self, newcap):
        new = [None] * newcap
        for i in range(self._n):
            new[i] = self._data[i]
        self._data = new
        self._cap = newcap

    def __repr__(self):
        return '[' + ','.join(str(self._data[i]) for i in range(self._n)) + ']'

if __name__ == '__main__':
    a = ArrayList()
    a.add(1); a.add(2); a.add(3)
    print(a.get(1))