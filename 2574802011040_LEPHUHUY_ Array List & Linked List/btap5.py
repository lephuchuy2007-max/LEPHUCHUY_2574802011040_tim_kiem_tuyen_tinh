"""
Bài 5: Duyệt và in phần tử; đếm theo điều kiện
"""
from btap1 import ArrayList

class ArrayList5(ArrayList):
    def for_each(self, fn):
        for i in range(self._n):
            fn(self._data[i])

    def count_if(self, predicate):
        cnt = 0
        for i in range(self._n):
            if predicate(self._data[i]):
                cnt += 1
        return cnt

if __name__ == '__main__':
    a = ArrayList5()
    for x in [1,2,3,4]: a.add(x)
    print(a.count_if(lambda x: x%2==0))