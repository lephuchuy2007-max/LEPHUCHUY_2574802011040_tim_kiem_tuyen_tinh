"""
Bài 20. Vì sao chọn m là số nguyên tố
Giải thích và minh họa vì sao chọn kích thước bảng m là số nguyên tố
(và tránh lũy thừa của 2) giúp phân bố đều hơn
"""

import math


def analyze_hash_distribution(keys, m, hash_name):
    """Phân tích phân bố hash"""
    buckets = [0] * m
    
    for key in keys:
        idx = key % m
        buckets[idx] += 1
    
    # Tính độ lệch chuẩn
    avg = sum(buckets) / m
    variance = sum((b - avg) ** 2 for b in buckets) / m
    std_dev = math.sqrt(variance)
    
    return {
        'name': hash_name,
        'm': m,
        'buckets': buckets,
        'avg': avg,
        'std_dev': std_dev,
        'max': max(buckets),
        'min': min(buckets)
    }


if __name__ == "__main__":
    print("=== VÌ SAO CHỌN m LÀ SỐ NGUYÊN TỐ ===\n")
    
    # Khóa test
    keys = list(range(100))
    
    # Test với m = 16 (lũy thừa của 2)
    print("Test 1: m = 16 (lũy thừa của 2)")
    result1 = analyze_hash_distribution(keys, 16, "Power of 2")
    print(f"m = {result1['m']}")
    print(f"Phân bố: {result1['buckets']}")
    print(f"Trung bình phần tử/bucket: {result1['avg']:.2f}")
    print(f"Độ lệch chuẩn: {result1['std_dev']:.2f}")
    print(f"Max/Min: {result1['max']}/{result1['min']}")
    print()
    
    # Test với m = 17 (số nguyên tố)
    print("Test 2: m = 17 (số nguyên tố)")
    result2 = analyze_hash_distribution(keys, 17, "Prime")
    print(f"m = {result2['m']}")
    print(f"Phân bố: {result2['buckets']}")
    print(f"Trung bình phần tử/bucket: {result2['avg']:.2f}")
    print(f"Độ lệch chuẩn: {result2['std_dev']:.2f}")
    print(f"Max/Min: {result2['max']}/{result2['min']}")
    print()
    
    # So sánh
    print("--- KẾT LUẬN ---")
    print(f"Độ lệch chuẩn (nhỏ = đều):")
    print(f"  m=16: {result1['std_dev']:.2f}")
    print(f"  m=17: {result2['std_dev']:.2f}")
    
    if result2['std_dev'] < result1['std_dev']:
        print(f"\n✓ m=17 (số nguyên tố) phân bố đều hơn m=16")
    
    print("\nNguyên nhân:")
    print("  - Lũy thừa của 2 có mối liên hệ với các khóa dạng 2^k")
    print("  - Số nguyên tố không có nhân tố chung với nhiều khóa")
    print("  - Phân bố đều hơn → ít va chạm hơn")
    
    print("\nHướng dẫn chọn m:")
    print("  ✓ Chọn số nguyên tố")
    print("  ✗ Tránh lũy thừa của 2")
    print("  ✗ Tránh số có nhiều ước (ví dụ 12, 20, 30...)")
