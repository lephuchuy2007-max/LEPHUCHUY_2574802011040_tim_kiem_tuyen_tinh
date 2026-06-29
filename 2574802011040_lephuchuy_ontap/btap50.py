import hashlib


class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        for i in range(self.hash_count):
            data = f'{item}-{i}'.encode()
            h = int(hashlib.md5(data).hexdigest(), 16)
            yield h % self.size

    def add(self, item):
        for idx in self._hashes(item):
            self.bit_array[idx] = 1

    def contains(self, item):
        return all(self.bit_array[idx] for idx in self._hashes(item))


if __name__ == '__main__':
    bf = BloomFilter(100, 3)
    bf.add('hello')
    print(bf.contains('hello'))
    print(bf.contains('world'))
