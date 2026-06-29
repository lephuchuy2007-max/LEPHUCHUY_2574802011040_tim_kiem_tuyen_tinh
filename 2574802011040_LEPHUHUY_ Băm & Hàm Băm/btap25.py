"""
Bài 25. Phương pháp nhân (multiplication method)
Cài đặt hàm băm theo phương pháp nhân
h(k) = floor(m · (k·A mod 1)) với 0<A<1
"""

def multiplication_hash(key, m, a=0.6180339887):
    """
    Phương pháp nhân
    
    h(k) = floor(m * fractional_part(k * A))
    
    Args:
        key: khóa cần hash
        m: kích thước bảng
        a: hệ số (thường dùng golden ratio ≈ 0.618)
    
    Returns:
        Chỉ số bucket (0 đến m-1)
    """
    # Tính k * A
    product = key * a
    
    # Lấy phần thập phân
    fractional = product - int(product)
    
    # Nhân với m và lấy phần nguyên
    return int(m * fractional)


def compare_multiplication_division():
    """So sánh phương pháp nhân vs chia"""
    
    keys = list(range(20))
    m = 11
    
    print("Key | Modulo (chia) | Multiply (nhân)")
    for key in keys:
        h_mod = key % m
        h_mul = multiplication_hash(key, m)
        print(f"{key:2d}  | {h_mod:2d}            | {h_mul:2d}")


if __name__ == "__main__":
    print("=== PHƯƠNG PHÁP NHÂN ===\n")
    
    # Ví dụ 1
    print("Ví dụ 1: multiplication_hash(37, 10)")
    result1 = multiplication_hash(37, 10)
    print(f"Kết quả: {result1}")
    
    # Ví dụ 2
    print("\nVí dụ 2: So sánh modulo vs nhân")
    compare_multiplication_division()
    
    print("\n--- PHÂN TÍCH ---")
    print("Phương pháp chia:")
    print("  h(k) = k mod m")
    print("  ✓ Đơn giản")
    print("  ✗ Kém khi m là lũy thừa của 2")
    
    print("\nPhương pháp nhân:")
    print("  h(k) = floor(m * (k*A mod 1))")
    print("  ✓ Phân bố tốt với bất kỳ m")
    print("  ✓ A = golden ratio (0.618...) công thức tối ưu")
    print("  ✗ Chậm hơn (phép nhân)")
    
    print("\nGolden ratio (φ):")
    print("  φ = (sqrt(5) - 1) / 2 ≈ 0.6180339887")
    print("  Có tính chất toán học đặc biệt cho phân bố đều")
