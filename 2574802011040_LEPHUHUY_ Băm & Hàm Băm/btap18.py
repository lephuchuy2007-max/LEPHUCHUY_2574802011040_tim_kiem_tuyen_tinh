"""
Bài 18. Hàm băm đa thức (polynomial)
Cài đặt polynomial rolling hash: h = (s[0]·p^(n-1) + ... + s[n-1]) mod m
Giải thích vai trò của p và m
"""

def polynomial_hash(s, p=31, m=10**9 + 7):
    """
    Polynomial hash cho chuỗi s
    
    h = (s[0]*p^(n-1) + s[1]*p^(n-2) + ... + s[n-1]) % m
    
    Args:
        s: chuỗi cần hash
        p: base (thường là số nguyên tố, vd 31 hoặc 37)
        m: modulo (thường là số nguyên tố lớn)
    
    Returns:
        Giá trị hash
    """
    hash_value = 0
    power = 1
    
    # Tính từ cuối chuỗi để tránh lũy thừa lớn
    for ch in reversed(s):
        hash_value = (hash_value + ord(ch) * power) % m
        power = (power * p) % m
    
    return hash_value


def polynomial_hash_forward(s, p=31, m=10**9 + 7):
    """Tính từ trước"""
    hash_value = 0
    for ch in s:
        hash_value = (hash_value * p + ord(ch)) % m
    return hash_value


if __name__ == "__main__":
    print("=== POLYNOMIAL HASH ===\n")
    
    # Ví dụ 1
    s1 = 'abc'
    h1 = polynomial_hash_forward(s1)
    print(f"polynomial_hash_forward('{s1}') = {h1}")
    
    # Ví dụ 2: Các đảo chữ có hash khác nhau
    print("\nVí dụ 2: Các đảo chữ có hash khác nhau")
    strings = ['abc', 'bca', 'cab', 'acb', 'bac', 'cba']
    print("Chuỗi | Hash")
    for s in strings:
        h = polynomial_hash_forward(s)
        print(f"{s:5} | {h}")
    
    print("\n--- VAI TRÒ CỦA p VÀ m ---")
    print("p (base):")
    print("  + Thường chọn số nguyên tố (31, 37, 97...)")
    print("  + Tạo sự khác biệt giữa các chuỗi khác nhau")
    print("  + p càng lớn, phân bố càng tốt")
    print("\nm (modulo):")
    print("  + Thường chọn số nguyên tố lớn (10^9+7)")
    print("  + Giảm xác suất va chạm (hash collision)")
    print("  + Giới hạn kích thước hash")
    
    # So sánh với hàm modulo đơn giản
    print("\n--- SO SÁNH VỚI HASH MODULO ---")
    m_simple = 10
    for s in ['abc', 'abc']:
        h_poly = polynomial_hash_forward(s, 31, m_simple)
        h_sum = sum(ord(ch) for ch in s) % m_simple
        print(f"'{s}': polynomial={h_poly}, sum={h_sum}")
