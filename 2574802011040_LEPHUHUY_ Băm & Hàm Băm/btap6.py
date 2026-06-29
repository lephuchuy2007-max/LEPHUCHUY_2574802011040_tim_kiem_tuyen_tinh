"""
Bài 6. So sánh chaining vs open addressing
Cài cả hai cách xử lý va chạm và so sánh: bộ nhớ, hiệu năng, cách xử lý xóa
"""

class ChainHashTable:
    """Xử lý va chạm bằng chaining"""
    def __init__(self, size=7):
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % len(self.table)

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
        self.count += 1

    def get(self, key, default=None):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return default

    def remove(self, key):
        idx = self._hash(key)
        self.table[idx] = [(k, v) for k, v in self.table[idx] if k != key]

    def stats(self):
        max_chain = max(len(b) for b in self.table)
        avg_chain = self.count / len(self.table)
        return {
            'buckets': len(self.table),
            'entries': self.count,
            'load_factor': self.count / len(self.table),
            'max_chain_length': max_chain,
            'avg_chain_length': avg_chain
        }


class OpenAddressingHashTable:
    """Xử lý va chạm bằng linear probing"""
    def __init__(self, size=7):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.tombstone = object()
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        while self.keys[index] is not None and self.keys[index] is not self.tombstone:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value
        self.count += 1

    def get(self, key, default=None):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return default

    def remove(self, key):
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = self.tombstone
                self.values[index] = None
                return
            index = (index + 1) % self.size

    def stats(self):
        used = sum(1 for k in self.keys if k is not None and k is not self.tombstone)
        tombstones = sum(1 for k in self.keys if k is self.tombstone)
        return {
            'table_size': self.size,
            'used_slots': used,
            'tombstone_slots': tombstones,
            'empty_slots': self.size - used - tombstones,
            'load_factor': used / self.size
        }


if __name__ == "__main__":
    print("=== SO SÁNH CHAINING vs OPEN ADDRESSING ===\n")
    
    chain = ChainHashTable(7)
    open_addr = OpenAddressingHashTable(7)
    
    print("Thêm 10 phần tử vào bảng kích thước 7:")
    for i in range(10):
        chain.put(f'key{i}', i)
        open_addr.put(f'key{i}', i)
    
    print("\n--- CHAINING STATS ---")
    stats_chain = chain.stats()
    for k, v in stats_chain.items():
        print(f"{k}: {v}")
    
    print("\n--- OPEN ADDRESSING STATS ---")
    stats_open = open_addr.stats()
    for k, v in stats_open.items():
        print(f"{k}: {v}")
    
    print("\n--- KẾT LUẬN ---")
    print("Chaining:")
    print("  + Không phải rehash khi tràn")
    print("  + Xóa phần tử dễ dàng (không cần tombstone)")
    print("  - Dùng thêm bộ nhớ cho con trỏ")
    print("  - Kém locality (truy cập tuần tự không tốt)")
    
    print("\nOpen Addressing:")
    print("  + Bộ nhớ liền tục (locality tốt hơn)")
    print("  + Không dùng thêm bộ nhớ con trỏ")
    print("  - Xóa phức tạp (cần tombstone)")
    print("  - Hiệu năng giảm khi load factor cao")
