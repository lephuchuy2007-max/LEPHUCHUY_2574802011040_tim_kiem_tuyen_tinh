"""
Bài 2: append (thêm cuối) và popBack (xóa cuối)
"""
from btap1 import ArrayList

class ArrayList2(ArrayList):
    def append(self, val):
        self.add(val)

    def popBack(self):
        if self._n == 0:
            raise IndexError('pop from empty')
        val = self._data[self._n-1]
        self._data[self._n-1] = None
        self._n -= 1
        return val

if __name__ == '__main__':
    a = ArrayList2()
    a.append(1); a.append(2); a.append(3)
    print(a.popBack())