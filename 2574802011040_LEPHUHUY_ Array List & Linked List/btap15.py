"""
Bài 15: Iterator và fail-fast
"""
from btap1 import ArrayList

class FailFastArrayList(ArrayList):
    def __init__(self):
        super().__init__()
        self._modCount = 0

    def add(self, val):
        super().add(val); self._modCount += 1

    def removeAt(self, idx):
        val = super()._data[idx]
        for i in range(idx, self._n-1): self._data[i]=self._data[i+1]
        self._data[self._n-1]=None; self._n-=1; self._modCount+=1

    def __iter__(self):
        expected = self._modCount
        i=0
        while i<self._n:
            if expected != self._modCount:
                raise RuntimeError('Concurrent modification')
            yield self._data[i]; i+=1

if __name__ == '__main__':
    a = FailFastArrayList()
    a.add(1); a.add(2)
    it = iter(a)
    print(next(it))
    a.add(3)
    try:
        print(next(it))
    except RuntimeError as e:
        print('caught',e)