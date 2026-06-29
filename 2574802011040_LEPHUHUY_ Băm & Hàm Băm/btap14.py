"""
Bài 14. Xóa lười trong open addressing
Cài đặt xóa lười (lazy deletion) bằng nhãn "đã xóa" (tombstone)
"""

class LazyDeletionHashTable:
    """Bảng băm với xóa lười sử dụng tombstone"""
    
    def __init__(self, size=11):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.deleted = object()  # Đánh dấu "đã xóa"
        self.count = 0
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        """Thêm hoặc cập nhật phần tử"""
        index = self._hash(key)
        
        while self.keys[index] is not None and self.keys[index] is not self.deleted:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        
        self.keys[index] = key
        self.values[index] = value
        self.count += 1
    
    def get(self, key, default=None):
        """Lấy giá trị của key"""
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        
        return default
    
    def remove(self, key):
        """Xóa lười: đánh dấu DELETED thay vì xóa hẳn"""
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = self.deleted  # Đánh dấu xóa
                self.values[index] = None
                return True
            index = (index + 1) % self.size
        
        return False
    
    def cleanup(self):
        """
        Dọn dẹp bảng bằng cách tạo bảng mới và chỉ thêm các phần tử chưa xóa
        """
        print(">>> Cleanup: xây dựng lại bảng")
        old_keys = self.keys
        old_values = self.values
        
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.count = 0
        
        for k, v in zip(old_keys, old_values):
            if k is not None and k is not self.deleted:
                self.put(k, v)
    
    def get_deleted_count(self):
        """Đếm số tombstone trong bảng"""
        return sum(1 for k in self.keys if k is self.deleted)


if __name__ == "__main__":
    ht = LazyDeletionHashTable(11)
    
    # Thêm phần tử
    print("Thêm phần tử:")
    ht.put('a', 1)
    ht.put('b', 2)
    ht.put('c', 3)
    print(f"Keys: {ht.keys}")
    
    # Xóa phần tử
    print("\nXóa 'b':")
    ht.remove('b')
    print(f"Keys: {ht.keys}")
    print(f"get('b'): {ht.get('b', 'NOT_FOUND')}")
    print(f"Tombstone count: {ht.get_deleted_count()}")
    
    # Thêm lại
    print("\nThêm 'd':")
    ht.put('d', 4)
    print(f"get('d'): {ht.get('d')}")
    
    # Dọn dẹp
    print("\nDọn dẹp bảng:")
    ht.cleanup()
    print(f"Keys: {ht.keys}")
    print(f"Tombstone count: {ht.get_deleted_count()}")
    
    print("\n--- PHÂN TÍCH ---")
    print("Ưu điểm xóa lười:")
    print("  + Xóa nhanh O(1)")
    print("  + Không cần rebuild lại bucket chains")
    print("\nNhược điểm:")
    print("  - Lãng phí bộ nhớ với tombstone")
    print("  - Cần cleanup định kỳ")
    print("  - Hiệu năng get/put giảm khi tombstone nhiều")
