"""
Bài 8: removeIf (xóa tại chỗ mọi phần tử thỏa điều kiện)
"""
from btap1 import ArrayList

class ArrayList8(ArrayList):
    def removeIf(self, predicate):
        write = 0
        for read in range(self._n):
            if not predicate(self._data[read]):
                self._data[write] = self._data[read]
                write += 1
        for i in range(write, self._n):
            self._data[i] = None
        removed = self._n - write
        self._n = write
        return removed

if __name__ == '__main__':
    a = ArrayList8()
    for x in [1,2,3,4]: a.add(x)
    a.removeIf(lambda x: x%2==0)
    print(a)