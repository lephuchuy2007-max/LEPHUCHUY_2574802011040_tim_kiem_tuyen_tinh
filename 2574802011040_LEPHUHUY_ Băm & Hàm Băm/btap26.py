"""
Bài 26. Hàm băm độc lập thứ tự
Thiết kế hàm băm cho một tập hợp (hoặc multiset)
sao cho kết quả không phụ thuộc thứ tự phần tử
"""

def hash_set_sum(items, mod=10**9 + 7):
    """
    Hash tập hợp bằng tổng hash các phần tử
    Độc lập thứ tự vì phép cộng không thứ tự
    """
    total = 0
    for item in items:
        total = (total + hash(item)) % mod
    return total


def hash_set_xor(items):
    """
    Hash tập hợp bằng XOR
    Cũng độc lập thứ tự vì XOR giao hoán
    """
    result = 0
    for item in items:
        result ^= hash(item)
    return result


def hash_set_product(items, mod=10**9 + 7):
    """
    Hash tập hợp bằng tích hash các phần tử
    Cũng độc lập thứ tự vì phép nhân giao hoán
    """
    result = 1
    for item in items:
        result = (result * hash(item)) % mod
    return result


def hash_frozenset(items):
    """Sử dụng frozenset (Python built-in)"""
    return hash(frozenset(items))


if __name__ == "__main__":
    print("=== HÀM BĂM ĐỘC LẬP THỨ TỰ ===\n")
    
    # Ví dụ 1: So sánh thứ tự khác nhau
    print("Ví dụ 1: hash({1,2,3}) = hash({3,1,2})?")
    
    items1 = [1, 2, 3]
    items2 = [3, 1, 2]
    
    h1_sum = hash_set_sum(items1)
    h2_sum = hash_set_sum(items2)
    print(f"Hàm tổng: {h1_sum} == {h2_sum} ? {h1_sum == h2_sum}")
    
    h1_xor = hash_set_xor(items1)
    h2_xor = hash_set_xor(items2)
    print(f"Hàm XOR: {h1_xor} == {h2_xor} ? {h1_xor == h2_xor}")
    
    h1_prod = hash_set_product(items1)
    h2_prod = hash_set_product(items2)
    print(f"Hàm tích: {h1_prod} == {h2_prod} ? {h1_prod == h2_prod}")
    
    h1_fs = hash_frozenset(items1)
    h2_fs = hash_frozenset(items2)
    print(f"Frozenset: {h1_fs} == {h2_fs} ? {h1_fs == h2_fs}")
    
    # Ví dụ 2
    print("\nVí dụ 2: Các thứ tự khác nhau")
    sets = [
        [1, 2, 3],
        [3, 1, 2],
        [2, 3, 1],
        [1, 3, 2]
    ]
    
    print("Tập | Hash_sum | Hash_xor | Hash_prod")
    for s in sets:
        h_sum = hash_set_sum(s)
        h_xor = hash_set_xor(s)
        h_prod = hash_set_product(s)
        print(f"{s} | {h_sum%10} | {h_xor%10} | {h_prod%10}")
    
    print("\n--- KẾT LUẬN ---")
    print("Phương pháp độc lập thứ tự:")
    print("  1. Sum: tổng các hash")
    print("  2. XOR: XOR các hash")
    print("  3. Product: tích các hash")
    print("  4. Frozenset: hash Python built-in (tối ưu)")
    print("\nAll have property: hash(set) = hash(any permutation)")
