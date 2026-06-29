"""
Bài 19. Đếm va chạm của một hàm băm
Cho một tập khóa và một hàm băm, đếm số va chạm
để đánh giá chất lượng phân bố
"""

def count_collisions(keys, hash_func, m):
    """
    Đếm số va chạm (collision) cho một tập khóa
    
    Va chạm: 2 khóa khác nhau có cùng hash
    """
    buckets = [0] * m
    
    for key in keys:
        idx = hash_func(key, m)
        buckets[idx] += 1
    
    # Đếm tổng số va chạm
    # Nếu bucket có n phần tử, có n-1 va chạm
    collisions = sum(max(0, count - 1) for count in buckets)
    
    return collisions, buckets


if __name__ == "__main__":
    print("=== ĐỀM VA CHẠM ===\n")
    
    # Hàm băm modulo
    def hash_mod(key, m):
        return key % m
    
    # Ví dụ 1: Phân bố tốt (ít va chạm)
    print("Ví dụ 1: Phân bố tốt")
    keys1 = [1, 2, 3, 4, 5]
    m1 = 10
    collisions1, buckets1 = count_collisions(keys1, hash_mod, m1)
    print(f"Keys: {keys1}")
    print(f"m: {m1}")
    print(f"Phân bố: {buckets1}")
    print(f"Số va chạm: {collisions1}")
    print()
    
    # Ví dụ 2: Phân bố kém (nhiều va chạm)
    print("Ví dụ 2: Phân bố kém")
    keys2 = [1, 11, 21, 31, 41, 51]
    m2 = 10
    collisions2, buckets2 = count_collisions(keys2, hash_mod, m2)
    print(f"Keys: {keys2}")
    print(f"m: {m2}")
    print(f"Phân bố: {buckets2}")
    print(f"Số va chạm: {collisions2}")
    print(f"Nhận xét: Tất cả keys cùng bucket → {collisions2} va chạm")
    
    # Ví dụ 3: So sánh 2 hàm băm
    print("\nVí dụ 3: So sánh 2 hàm băm")
    keys3 = list(range(20))
    
    print("Hàm băm 1: h(k) = k % 16 (lũy thừa của 2)")
    collisions3a, buckets3a = count_collisions(keys3, hash_mod, 16)
    print(f"  Số va chạm: {collisions3a}")
    print(f"  Phân bố: {buckets3a}")
    
    print("\nHàm băm 2: h(k) = k % 17 (số nguyên tố)")
    collisions3b, buckets3b = count_collisions(keys3, hash_mod, 17)
    print(f"  Số va chạm: {collisions3b}")
    print(f"  Phân bố: {buckets3b[:5]}... (đều hơn)")
