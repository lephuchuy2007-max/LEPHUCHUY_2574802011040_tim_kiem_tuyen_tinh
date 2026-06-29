"""
Bài 7. Hệ số tải và rehashing
Khi load factor = n/m vượt ngưỡng (vd 0.75), cấp phát bảng lớn hơn và băm lại toàn bộ
"""

class DynamicHashTable:
    """Bảng băm với cơ chế rehashing tự động"""
    
    def __init__(self, initial_size=4, threshold=0.75):
        self.threshold = threshold
        self.size = initial_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        # Kiểm tra cần rehash hay không
        if self.count / self.size >= self.threshold:
            self._rehash(self.size * 2)
        
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
    
    def _rehash(self, new_size):
        """Rehash tất cả phần tử với kích thước bảng mới"""
        print(f">>> Rehashing: {self.size} → {new_size}")
        
        # Lưu tất cả phần tử cũ
        old_items = [(k, v) for bucket in self.table for k, v in bucket]
        
        # Tạo bảng mới
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        self.count = 0
        
        # Thêm lại tất cả phần tử
        for k, v in old_items:
            self.put(k, v)
    
    def get_load_factor(self):
        return self.count / self.size
    
    def __repr__(self):
        return f"Size={self.size}, Count={self.count}, Load_factor={self.get_load_factor():.2f}"


if __name__ == "__main__":
    print("Khởi tạo bảng với size=4, threshold=0.75\n")
    ht = DynamicHashTable(4, 0.75)
    
    for i in range(10):
        ht.put(f'key{i}', i)
        print(f"Sau khi thêm key{i}: {ht}")
    
    print(f"\nGiá trị cuối cùng: size={ht.size}, entries={ht.count}")
