class HashTableRehashing:
    def __init__(self, capacity=8, load_factor=0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_items = [(k, v) for entry in self.table if entry for (k, v) in [entry]]
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0
        for k, v in old_items:
            self.put(k, v)

    def put(self, key, value):
        if self.size + 1 > self.capacity * self.load_factor:
            self._resize()
        idx = self._hash(key)
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.capacity
        self.table[idx] = (key, value)
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        start = idx
        while self.table[idx] is not None:
            if self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.capacity
            if idx == start:
                break
        return None


if __name__ == '__main__':
    ht = HashTableRehashing()
    ht.put('a', 1)
    ht.put('b', 2)
    print(ht.get('a'), ht.get('b'))
