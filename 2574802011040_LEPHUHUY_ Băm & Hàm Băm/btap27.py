"""
Bài 27. Tấn công hash flooding
Minh họa tấn công hash flooding: tạo nhiều khóa cùng bucket khiến bảng suy biến
Cách phòng chống
"""

import time


class SimpleHashTable:
    """Bảng băm đơn giản (dễ bị tấn công)"""
    def __init__(self, m=11):
        self.m = m
        self.table = [[] for _ in range(m)]
    
    def _hash(self, key):
        return key % self.m
    
    def put(self, key):
        idx = self._hash(key)
        if key not in self.table[idx]:
            self.table[idx].append(key)
    
    def get(self, key):
        idx = self._hash(key)
        return key in self.table[idx]


class SecureHashTable:
    """Bảng băm an toàn (chống tấn công)"""
    import random
    
    def __init__(self, m=11):
        self.m = m
        self.table = [[] for _ in range(m)]
        # Khóa bí mật ngẫu nhiên
        self.seed = random.random()
    
    def _hash(self, key):
        # Sử dụng khóa bí mật trong hash
        return int((key * self.seed) % self.m)
    
    def put(self, key):
        idx = self._hash(key)
        if key not in self.table[idx]:
            self.table[idx].append(key)
    
    def get(self, key):
        idx = self._hash(key)
        return key in self.table[idx]


if __name__ == "__main__":
    print("=== TẤN CÔNG HASH FLOODING ===\n")
    
    print("Ví dụ 1: Tấn công hash table đơn giản")
    print("-" * 50)
    
    ht = SimpleHashTable(11)
    
    # Tạo khóa xấu (tất cả % 11 == 0)
    bad_keys = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
    
    print(f"Thêm khóa xấu: {bad_keys}")
    print(f"Tất cả khóa cùng bucket (idx = 0)")
    
    start = time.time()
    for key in bad_keys:
        ht.put(key)
    simple_time = time.time() - start
    
    start = time.time()
    # Tìm kiếm trong danh sách dài (O(n) thay vì O(1))
    for key in bad_keys:
        ht.get(key)
    simple_search = time.time() - start
    
    print(f"Phân bố: {[len(b) for b in ht.table]}")
    print(f"Thời gian insert: {simple_time*1000:.4f}ms")
    print(f"Thời gian search: {simple_search*1000:.4f}ms")
    print(f"Hiệu năng: O(n) thay vì O(1)")
    
    print("\n" + "=" * 50)
    print("Ví dụ 2: Phòng chống bằng hashing ngẫu nhiên")
    print("-" * 50)
    
    ht_secure = SecureHashTable(11)
    
    print(f"Thêm khóa xấu với hashing ngẫu nhiên")
    
    start = time.time()
    for key in bad_keys:
        ht_secure.put(key)
    secure_time = time.time() - start
    
    start = time.time()
    for key in bad_keys:
        ht_secure.get(key)
    secure_search = time.time() - start
    
    print(f"Phân bố: {[len(b) for b in ht_secure.table]}")
    print(f"Thời gian insert: {secure_time*1000:.4f}ms")
    print(f"Thời gian search: {secure_search*1000:.4f}ms")
    print(f"Hiệu năng: O(1) được phục hồi")
    
    print("\n--- KẾT LUẬN ---")
    print("Hash Flooding Attack:")
    print("  + Tấn công dựa trên tìm nhiều khóa cùng bucket")
    print("  + Khiến bảng băm suy biến thành O(n) per operation")
    print("\nPhòng chống:")
    print("  1. Universal Hashing: hàm hash ngẫu nhiên")
    print("  2. Cryptographic hash: MD5, SHA-256")
    print("  3. Randomized seed: thay đổi seed mỗi lần run")
    print("  4. Limit chain length: rebuild khi chain quá dài")
