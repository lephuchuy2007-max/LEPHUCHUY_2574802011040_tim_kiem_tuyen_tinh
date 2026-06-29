class HashTableChaining:
    def __init__(self, size=8):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, _) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def remove(self, key):
        idx = self._hash(key)
        self.table[idx] = [(k, v) for k, v in self.table[idx] if k != key]


class HashTableOpenAddressing:
    def __init__(self, size=8):
        self.size = size
        self.table = [None] * size
        self.deleted = object()

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        while self.table[idx] is not None and self.table[idx] is not self.deleted and self.table[idx][0] != key:
            idx = (idx + 1) % self.size
        self.table[idx] = (key, value)

    def get(self, key):
        idx = self._hash(key)
        start = idx
        while self.table[idx] is not None:
            if self.table[idx] is not self.deleted and self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size
            if idx == start:
                break
        return None

    def remove(self, key):
        idx = self._hash(key)
        start = idx
        while self.table[idx] is not None:
            if self.table[idx] is not self.deleted and self.table[idx][0] == key:
                self.table[idx] = self.deleted
                return
            idx = (idx + 1) % self.size
            if idx == start:
                break


if __name__ == '__main__':
    ht = HashTableChaining()
    ht.put('a', 1)
    ht.put('b', 2)
    print(ht.get('a'), ht.get('b'))
    ht2 = HashTableOpenAddressing()
    ht2.put('a', 1)
    ht2.put('b', 2)
    print(ht2.get('a'), ht2.get('b'))
