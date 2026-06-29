"""
Bài 24. Băm phổ quát (Universal Hashing)
Cài đặt một họ hàm băm phổ quát
h(k) = ((a·k + b) mod p) mod m với a, b ngẫu nhiên
"""

import random


class UniversalHashFamily:
    """Họ hàm băm phổ quát"""
    
    def __init__(self, m, p=None):
        """
        m: kích thước bảng
        p: số nguyên tố lớn hơn giá trị max của key
        """
        self.m = m
        # Nếu không chỉ định p, dùng số nguyên tố lớn
        self.p = p or 10007
        
        # Chọn a, b ngẫu nhiên
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
    
    def hash(self, key):
        """Tính hash của key"""
        return ((self.a * key + self.b) % self.p) % self.m
    
    def __repr__(self):
        return f"UH(a={self.a}, b={self.b})"


class UniversalHashTable:
    """Bảng băm dùng universal hashing"""
    
    def __init__(self, m=11):
        self.m = m
        self.hash_func = UniversalHashFamily(m)
        self.table = [[] for _ in range(m)]
    
    def put(self, key, value):
        idx = self.hash_func.hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))
    
    def get(self, key, default=None):
        idx = self.hash_func.hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return default


if __name__ == "__main__":
    print("=== UNIVERSAL HASHING ===\n")
    
    # Ví dụ 1: Tạo nhiều hàm băm khác nhau
    print("Ví dụ 1: 3 hàm băm từ cùng họ phổ quát")
    m = 11
    for i in range(3):
        h = UniversalHashFamily(m)
        keys = [1, 2, 3, 4, 5]
        hashes = [h.hash(k) for k in keys]
        print(f"  {h}: {list(zip(keys, hashes))}")
    
    # Ví dụ 2: Chọng đầu vào xấu
    print("\nVí dụ 2: Phòng chống tấn công hash flooding")
    
    # Khóa xấu (tất cả cùng hash với hàm modulo)
    bad_keys = [0, 11, 22, 33, 44]  # Tất cả % 11 = 0
    
    print(f"Bad keys (modulo 11): {bad_keys}")
    print(f"Với modulo: tất cả hash = 0")
    
    print("\nVới universal hash:")
    uh = UniversalHashFamily(11)
    hashes = [uh.hash(k) for k in bad_keys]
    print(f"Hashes: {hashes}")
    print(f"Phân bố: tốt hơn (ngẫu nhiên)")
    
    # Ví dụ 3: Bảng băm
    print("\nVí dụ 3: Bảng băm phổ quát")
    ht = UniversalHashTable(11)
    for i in range(10):
        ht.put(i, i * 10)
    
    for i in range(5):
        print(f"get({i}) = {ht.get(i)}")
    
    print("\n--- PHÂN TÍCH ---")
    print("Universal Hashing:")
    print("  + Chống lại tấn công hash flooding")
    print("  + Xác suất va chạm = 1/m (lý thuyết)")
    print("  + A, b thay đổi mỗi lần khởi tạo")
    print("\nNhược điểm:")
    print("  - Chậm hơn hash modulo (có phép nhân)")
    print("  - Cần lưu a, b")
