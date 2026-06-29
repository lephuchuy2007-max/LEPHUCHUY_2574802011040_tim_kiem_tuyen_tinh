"""
Bài 14: Mảng động 2 chiều (dynamic matrix)
"""
class DynamicMatrix:
    def __init__(self, rows=0, cols=0):
        self._rows = rows
        self._cols = cols
        self._data = [[None]*cols for _ in range(rows)]

    def add_row(self, row=None):
        if row is None:
            row = [None]*self._cols
        if len(row) != self._cols:
            raise ValueError('row length mismatch')
        self._data.append(list(row))
        self._rows += 1

    def set(self,i,j,val):
        self._data[i][j]=val

    def get(self,i,j):
        return self._data[i][j]

if __name__ == '__main__':
    m = DynamicMatrix(1,3)
    m.set(0,1,9)
    m.add_row([1,2,3])
    print(m.get(1,2))