"""
Bài 22. Hàm băm cho cặp / tuple
Thiết kế hàm băm cho cặp (a, b) hoặc tuple
Kết hợp hash thành phần sao cho ít va chạm
"""

def hash_pair(a, b, p=31, mod=10**9 + 7):
    """
    Hàm băm cho cặp (a, b)
    h(a, b) = (h(a) * p + h(b)) % mod
    """
    ha = hash(a)
    hb = hash(b)
    return (ha * p + hb) % mod


def hash_pair_xor(a, b):
    """
    Hàm băm cho cặp sử dụng XOR
    h(a, b) = h(a) XOR h(b)
    Nhược điểm: hash(a,b) == hash(b,a) nếu a==b, không tốt
    """
    return hash(a) ^ hash(b)


def hash_pair_mix(a, b, mod=10**9 + 7):
    """
    Hàm băm kết hợp (mix) tốt hơn
    Sử dụng prime combinations
    """
    ha = abs(hash(a))
    hb = abs(hash(b))
    return (ha * 1000000007 + hb) % mod


def hash_tuple(items, p=31, mod=10**9 + 7):
    """
    Hàm băm cho tuple (mở rộng cho nhiều phần tử)
    """
    result = 0
    for item in items:
        result = (result * p + hash(item)) % mod
    return result


if __name__ == "__main__":
    print("=== HÀM BĂM CHO CẶP / TUPLE ===\n")
    
    # Ví dụ 1
    print("Ví dụ 1: Hash cho cặp (2, 3)")
    h1 = hash_pair(2, 3)
    print(f"hash_pair(2, 3) = {h1}")
    
    # Ví dụ 2: So sánh các phương pháp
    print("\nVí dụ 2: So sánh các phương pháp")
    pairs = [(1, 2), (2, 3), (3, 4), (1, 3), (2, 1)]
    
    print("Cặp | hash_pair | hash_xor | hash_mix")
    for a, b in pairs:
        h1 = hash_pair(a, b)
        h2 = hash_pair_xor(a, b)
        h3 = hash_pair_mix(a, b)
        print(f"({a},{b}) | {h1:10} | {h2:8} | {h3:10}")
    
    # Ví dụ 3: Hash cho tuple
    print("\nVí dụ 3: Hash cho tuple")
    tuples = [(1,), (1,2), (1,2,3), (1,2,3,4)]
    for t in tuples:
        h = hash_tuple(t)
        print(f"hash_tuple{t} = {h}")
    
    print("\n--- GIỚI THIỆU ---")
    print("Phương pháp hash cặp:")
    print("  1. Polynomial combination: (ha * p + hb) % mod")
    print("     ✓ Thứ tự quan trọng")
    print("     ✓ Phân bố tốt")
    print("\n  2. XOR: ha XOR hb")
    print("     ✓ Nhanh")
    print("     ✗ Mất thứ tự [(a,b) == (b,a) nếu a==b]")
    print("\n  3. Mix: (ha * prime + hb) % mod")
    print("     ✓ Phân bố rất tốt")
    print("     ✗ Chậm hơn XOR")
