"""
Bài 9: Đảo ngược tại chỗ
"""
from btap1 import ArrayList

class ArrayList9(ArrayList):
    def reverse(self):
        i, j = 0, self._n-1
        while i < j:
            self._data[i], self._data[j] = self._data[j], self._data[i]
            i += 1; j -= 1

if __name__ == '__main__':
    a = ArrayList9()
    for x in [1,2,3,4]: a.add(x)
    a.reverse(); print(a)