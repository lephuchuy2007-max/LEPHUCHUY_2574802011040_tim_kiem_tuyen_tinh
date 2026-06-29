"""
Bài 23. So sánh chất lượng phân bố
So sánh hai hàm băm trên cùng tập khóa bằng cách đếm phần tử mỗi bucket
và tính độ lệch (thống kê chi-square)
"""

import math


def chi_square(observed, expected):
    """Tính chi-square statistic"""
    chi_sq = 0
    for o, e in zip(observed, expected):
        if e > 0:
            chi_sq += (o - e) ** 2 / e
    return chi_sq


def analyze_hash_quality(keys, hash_func, m, name):
    """Phân tích chất lượng hàm băm"""
    buckets = [0] * m
    
    for key in keys:
        idx = hash_func(key, m)
        buckets[idx] += 1
    
    # Tính thống kê
    n = len(keys)
    expected = n / m
    
    variance = sum((b - expected) ** 2 for b in buckets) / m
    std_dev = math.sqrt(variance)
    chi_sq = chi_square(buckets, [expected] * m)
    
    return {
        'name': name,
        'buckets': buckets,
        'mean': expected,
        'std_dev': std_dev,
        'chi_square': chi_sq,
        'max': max(buckets),
        'min': min(buckets),
        'max_min_ratio': max(buckets) / min(buckets) if min(buckets) > 0 else float('inf')
    }


if __name__ == "__main__":
    print("=== SO SÁNH CHẤT LƯỢNG PHÂN BỐ ===\n")
    
    # Khóa test
    keys = [i for i in range(100)]
    m = 11
    
    # Hàm băm 1: modulo đơn giản
    def hash1(key, m):
        return key % m
    
    # Hàm băm 2: polynomial
    def hash2(key, m):
        p = 31
        return (key * p) % m
    
    # Phân tích
    result1 = analyze_hash_quality(keys, hash1, m, "Modulo")
    result2 = analyze_hash_quality(keys, hash2, m, "Polynomial")
    
    print(f"Tập khóa: 0 đến 99 ({len(keys)} khóa)")
    print(f"Kích thước bảng: {m}\n")
    
    print("=== HÀM BĂM 1: Modulo ===")
    print(f"Phân bố: {result1['buckets']}")
    print(f"Trung bình: {result1['mean']:.2f}")
    print(f"Độ lệch chuẩn: {result1['std_dev']:.2f}")
    print(f"Chi-square: {result1['chi_square']:.2f}")
    print(f"Max/Min bucket: {result1['max']}/{result1['min']} = {result1['max_min_ratio']:.2f}")
    
    print("\n=== HÀM BĂM 2: Polynomial ===")
    print(f"Phân bố: {result2['buckets']}")
    print(f"Trung bình: {result2['mean']:.2f}")
    print(f"Độ lệch chuẩn: {result2['std_dev']:.2f}")
    print(f"Chi-square: {result2['chi_square']:.2f}")
    print(f"Max/Min bucket: {result2['max']}/{result2['min']} = {result2['max_min_ratio']:.2f}")
    
    print("\n--- KẾT LUẬN ---")
    print("Hàm băm tốt: Độ lệch chuẩn nhỏ, chi-square thấp, max/min gần 1")
    if result1['chi_square'] < result2['chi_square']:
        winner = "Modulo"
    else:
        winner = "Polynomial"
    print(f"✓ {winner} phân bố tốt hơn")
