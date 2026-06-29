"""
Bài 21. Rolling hash & Rabin–Karp
Dùng rolling hash để tìm một chuỗi mẫu trong văn bản
Thuật toán Rabin–Karp trong O(n+m) trung bình
"""

def rabin_karp(text, pattern, base=31, mod=10**9 + 7):
    """
    Tìm tất cả vị trí xuất hiện của pattern trong text
    sử dụng Rabin-Karp algorithm
    """
    if not pattern or not text or len(pattern) > len(text):
        return []
    
    n = len(text)
    m = len(pattern)
    
    # Tính hash của pattern
    pattern_hash = 0
    text_hash = 0
    base_m = 1  # base^(m-1) % mod
    
    # Tính base^(m-1)
    for _ in range(m - 1):
        base_m = (base_m * base) % mod
    
    # Tính hash của pattern và cửa sổ đầu tiên
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % mod
        text_hash = (text_hash * base + ord(text[i])) % mod
    
    # Dò tìm
    matches = []
    for i in range(n - m + 1):
        # Nếu hash bằng, kiểm tra xem chuỗi thật có bằng không
        if pattern_hash == text_hash:
            if text[i:i+m] == pattern:
                matches.append(i)
        
        # Rolling hash cho cửa sổ tiếp theo
        if i < n - m:
            # Xóa ký tự trái, thêm ký tự phải
            text_hash = (text_hash - ord(text[i]) * base_m) % mod
            text_hash = (text_hash * base + ord(text[i + m])) % mod
            text_hash = (text_hash + mod) % mod  # Đảm bảo dương
    
    return matches


if __name__ == "__main__":
    print("=== RABIN-KARP ALGORITHM ===\n")
    
    # Ví dụ 1
    text1 = 'zabcd'
    pattern1 = 'abc'
    matches1 = rabin_karp(text1, pattern1)
    print(f"Text: '{text1}'")
    print(f"Pattern: '{pattern1}'")
    print(f"Matches tại: {matches1}")
    # Output: [1]
    
    # Ví dụ 2: Nhiều lần xuất hiện
    print("\nVí dụ 2:")
    text2 = 'ababcdabab'
    pattern2 = 'ab'
    matches2 = rabin_karp(text2, pattern2)
    print(f"Text: '{text2}'")
    print(f"Pattern: '{pattern2}'")
    print(f"Matches tại: {matches2}")
    # Output: [0, 6, 8]
    
    # Ví dụ 3: Không tìm thấy
    print("\nVí dụ 3:")
    text3 = 'hello world'
    pattern3 = 'xyz'
    matches3 = rabin_karp(text3, pattern3)
    print(f"Text: '{text3}'")
    print(f"Pattern: '{pattern3}'")
    print(f"Matches tại: {matches3}")
    # Output: []
    
    print("\n--- PHÂN TÍCH RABIN-KARP ---")
    print("Ưu điểm:")
    print("  + Trung bình O(n+m)")
    print("  + Tốt cho tìm kiếm multiple patterns")
    print("  + Hoạt động tốt khi văn bản lớn")
    print("\nNhược điểm:")
    print("  - Xấu nhất O(nm) nếu có nhiều false positive")
    print("  - Cần tính hash cẩn thận")
