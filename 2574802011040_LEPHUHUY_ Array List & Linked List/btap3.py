"""
Bài 3: Chèn / xóa ở vị trí bất kỳ
"""
from btap1 import ArrayList

class ArrayList3(ArrayList):
    def insert(self, idx, val):
        if idx < 0 or idx > self._n:
            raise IndexError('index out of range')
        if self._n == self._cap:
            self._resize(self._cap * 2)
        # shift
        for i in range(self._n, idx, -1):
            self._data[i] = self._data[i-1]
        self._data[idx] = val
        self._n += 1

    def removeAt(self, idx):
        self._check_index(idx)
        val = self._data[idx]
        for i in range(idx, self._n-1):
            self._data[i] = self._data[i+1]
        self._data[self._n-1] = None
        self._n -= 1
        return val

if __name__ == '__main__':
    a = ArrayList3()
    a.add(1); a.add(2); a.add(4)
    a.insert(2,3)
    print(a)