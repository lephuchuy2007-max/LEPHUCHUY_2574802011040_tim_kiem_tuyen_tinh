"""
Bài 17. Hàm băm cho chuỗi (tổng mã ký tự)
Cài đặt hàm băm cho chuỗi bằng tổng mã ký tự rồi lấy mod m
Chỉ ra nhược điểm (các đảo chữ cho cùng giá trị)
"""

def hash_string_sum(s, m):
    """
    Hàm băm chuỗi bằng tổng mã ký tự
    Nhược điểm: các đảo chữ (anagrams) có hash giống nhau
    """
    total = 0
    for ch in s:
        total += ord(ch)
    return total % m


if __name__ == "__main__":
    m = 10
    
    # Ví dụ 1
    s1 = 'abc'
    print(f"hash_string_sum('{s1}', {m}) = {hash_string_sum(s1, m)}")
    
    # Ví dụ 2: Các đảo chữ có hash giống nhau
    print("\nVí dụ 2: Vấn đề của hàm băm tổng")
    strings = ['abc', 'bca', 'cab', 'acb', 'bac', 'cba']
    hashes = [hash_string_sum(s, m) for s in strings]
    
    print("Chuỗi | Hash")
    for s, h in zip(strings, hashes):
        print(f"{s:5} | {h}")
    
    print("\nNhận xét: Tất cả đảo chữ có hash = 6")
    print("Nguyên nhân: Phép cộng không thứ tự")
    print("  ord('a') + ord('b') + ord('c') = 97 + 98 + 99 = 294")
    print("  Bất kỳ thứ tự nào cũng cho tổng 294")
    print("  294 % 10 = 4")
    
    # Sửa lỗi
    print("\n--- GIẢI PHÁP: POLYNOMIAL HASH ---")
    print("Dùng hàm đa thức: h = (a[0]*p^(n-1) + a[1]*p^(n-2) + ... + a[n-1]) % m")
