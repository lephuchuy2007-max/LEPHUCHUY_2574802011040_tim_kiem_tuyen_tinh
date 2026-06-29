"""
Bài 29. Bloom Filter
Cài đặt Bloom filter dùng nhiều hàm băm để kiểm tra thành viên xấp xỉ
Phân tích xác suất dương tính giả theo số hàm băm k và kích thước bit m
"""

import math


class BloomFilter:
    """Bloom Filter: kiểm tra thành viên xấp xỉ"""
    
    def __init__(self, size=100, hash_count=3):
        """
        size: số bit trong bộ lọc
        hash_count: số hàm băm
        """
        self.size = size
        self.hash_count = hash_count
        self.bits = [0] * size
    
    def _hashes(self, item):
        """Tính k hashes cho item"""
        hashes = []
        for i in range(self.hash_count):
            h = abs(hash((item, i))) % self.size
            hashes.append(h)
        return hashes
    
    def add(self, item):
        """Thêm item vào Bloom Filter"""
        for h in self._hashes(item):
            self.bits[h] = 1
    
    def contains(self, item):
        """Kiểm tra item có trong filter hay không"""
        return all(self.bits[h] == 1 for h in self._hashes(item))
    
    def false_positive_rate(self, num_items):
        """Tính xác suất dương tính giả lý thuyết"""
        # P = (1 - (1 - 1/m)^(k*n))^k
        # ≈ (1 - e^(-k*n/m))^k
        k = self.hash_count
        n = num_items
        m = self.size
        
        if m == 0:
            return 1.0
        
        # Sử dụng xấp xỉ
        exponent = -k * n / m
        prob = 1 - math.exp(exponent)
        return prob ** k


if __name__ == "__main__":
    print("=== BLOOM FILTER ===\n")
    
    # Ví dụ 1: Sử dụng cơ bản
    print("Ví dụ 1: Bloom Filter cơ bản")
    bf = BloomFilter(size=20, hash_count=3)
    
    # Thêm phần tử
    words = ['apple', 'banana', 'cherry']
    for word in words:
        bf.add(word)
    
    # Kiểm tra
    print(f"Thêm: {words}")
    print(f"contains('apple'): {bf.contains('apple')}")  # True
    print(f"contains('banana'): {bf.contains('banana')}")  # True
    print(f"contains('date'): {bf.contains('date')}")  # False (đúng)
    print(f"contains('xyz'): {bf.contains('xyz')}")  # False
    
    # Ví dụ 2: Xác suất dương tính giả
    print("\n" + "=" * 50)
    print("Ví dụ 2: Xác suất dương tính giả")
    
    # So sánh các cấu hình
    configs = [
        (100, 3),
        (100, 5),
        (100, 7),
        (50, 3),
        (200, 3)
    ]
    
    print(f"{'Size':<6} {'k':<3} {'Items':<8} {'FP Rate':<12} {'Insight':<20}")
    print("-" * 60)
    
    for size, k in configs:
        bf_test = BloomFilter(size, k)
        n = size // (k * math.log(2) ** 2)  # Công thức tối ưu
        fpr = bf_test.false_positive_rate(int(n))
        print(f"{size:<6} {k:<3} {int(n):<8} {fpr:.4f}       ", end="")
        if fpr < 0.01:
            print("Tốt")
        elif fpr < 0.05:
            print("Chấp nhận")
        else:
            print("Kém")
    
    # Ví dụ 3: Độ cao nhất
    print("\n" + "=" * 50)
    print("Ví dụ 3: Chiếc cao nhất")
    
    # Công thức tối ưu k = (m/n) * ln(2)
    m = 100
    n = 20
    k_optimal = int((m / n) * math.log(2))
    
    print(f"Size: {m}, Items: {n}")
    print(f"k tối ưu: {k_optimal}")
    
    bf_opt = BloomFilter(m, k_optimal)
    fpr_opt = bf_opt.false_positive_rate(n)
    print(f"FP Rate: {fpr_opt:.4f}")
    
    print("\n--- PHÂN TÍCH ---")
    print("Bloom Filter:")
    print("  ✓ Không âm tính giả (nếu có → chắc chắn có)")
    print("  ✓ Có thể dương tính giả (báo có nhưng thực chưa có)")
    print("  ✓ Bộ nhớ rất nhỏ so với set thường")
    print("  ✓ Tìm kiếm O(k)")
    print("\nTrường hợp dùng:")
    print("  - Kiểm tra phần tử có trong tập lớn")
    print("  - Cache-like checking")
    print("  - Network routing")
