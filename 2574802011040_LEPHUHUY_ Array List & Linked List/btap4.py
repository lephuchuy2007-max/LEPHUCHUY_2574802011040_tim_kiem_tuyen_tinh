"""
Bài 4: Tìm kiếm tuyến tính (indexOf)
"""
from btap1 import ArrayList

class ArrayList4(ArrayList):
    def indexOf(self, val):
        for i in range(self._n):
            if self._data[i] == val:
                return i
        return -1

if __name__ == '__main__':
    a = ArrayList4()
    a.add(5); a.add(3); a.add(7)
    print(a.indexOf(7))