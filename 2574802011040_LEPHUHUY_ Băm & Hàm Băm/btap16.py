"""
Bài 16 (PHẦN B - HÀM BĂM). Hàm băm modulo cho số nguyên
Cài đặt hàm băm đơn giản h(k) = k mod m
Tính chỉ số bucket và quan sát phân bố
"""

def hash_modulo(key, m):
    """Hàm băm modulo đơn giản"""
    return key % m


def analyze_distribution(keys, m):
    """Phân tích phân bố của keys"""
    buckets = [0] * m
    
    for key in keys:
        idx = hash_modulo(key, m)
        buckets[idx] += 1
    
    return buckets


if __name__ == "__main__":
    # Ví dụ 1: k=37, m=10
    print("Ví dụ 1:")
    print(f"hash_modulo(37, 10) = {hash_modulo(37, 10)}")
    # Output: 7
    
    # Ví dụ 2: Phân tích phân bố
    print("\nVí dụ 2: Phân tích phân bố")
    keys = [37, 47, 57, 67, 77, 87, 97]  # Tất cả đều = 7 (mod 10)
    m = 10
    distribution = analyze_distribution(keys, m)
    print(f"Keys: {keys}")
    print(f"m: {m}")
    print(f"Phân bố: {distribution}")
    print(f"Vấn đề: Tất cả khóa cùng bucket (kém phân bố)")
    
    # Ví dụ 3: Phân bố tốt
    print("\nVí dụ 3: Phân bố tốt")
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    distribution = analyze_distribution(keys, 10)
    print(f"Keys: {keys}")
    print(f"Phân bố: {distribution}")
    print(f"Nhận xét: Phân bố đều (tốt)")
