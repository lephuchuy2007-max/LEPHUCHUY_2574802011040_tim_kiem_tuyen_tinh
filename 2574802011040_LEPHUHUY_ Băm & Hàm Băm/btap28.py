"""
Bài 28. Rolling hash 2 chiều
Mở rộng rolling hash để tìm một ma trận con trong ma trận lớn
(2D pattern matching)
"""


def matrix_rolling_hash(text_matrix, pattern_matrix, base=31, mod=10**9 + 7):
    """
    Tìm vị trí của pattern_matrix trong text_matrix sử dụng rolling hash 2D
    """
    if not pattern_matrix or not text_matrix:
        return []
    
    rows_t = len(text_matrix)
    cols_t = len(text_matrix[0])
    rows_p = len(pattern_matrix)
    cols_p = len(pattern_matrix[0])
    
    if rows_t < rows_p or cols_t < cols_p:
        return []
    
    # Tính hash của pattern
    pattern_hash = compute_matrix_hash(pattern_matrix, base, mod)
    
    matches = []
    
    # Dò tìm trong text_matrix
    for i in range(rows_t - rows_p + 1):
        for j in range(cols_t - cols_p + 1):
            # Lấy submatrix
            sub = [text_matrix[i+r][j:j+cols_p] for r in range(rows_p)]
            
            # Tính hash
            sub_hash = compute_matrix_hash(sub, base, mod)
            
            # Kiểm tra va chạm hash
            if sub_hash == pattern_hash:
                # Kiểm tra xem ma trận thật có bằng không
                if sub == pattern_matrix:
                    matches.append((i, j))
    
    return matches


def compute_matrix_hash(matrix, base=31, mod=10**9 + 7):
    """Tính hash của ma trận"""
    hash_value = 0
    
    for row in matrix:
        row_hash = 0
        for val in row:
            row_hash = (row_hash * base + val) % mod
        hash_value = (hash_value * base + row_hash) % mod
    
    return hash_value


if __name__ == "__main__":
    print("=== ROLLING HASH 2 CHIỀU ===\n")
    
    # Ví dụ 1: Ma trận nhỏ
    print("Ví dụ 1: Tìm ma trận con 2x2")
    text = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]
    ]
    pattern = [
        [0, 1],
        [1, 0]
    ]
    
    print("Text matrix:")
    for row in text:
        print(f"  {row}")
    
    print("\nPattern matrix:")
    for row in pattern:
        print(f"  {row}")
    
    matches = matrix_rolling_hash(text, pattern)
    print(f"\nMatches tại: {matches}")
    
    # Ví dụ 2
    print("\n" + "=" * 50)
    print("Ví dụ 2: Tìm ma trận con 1x2")
    pattern2 = [[1, 0]]
    matches2 = matrix_rolling_hash(text, pattern2)
    print(f"Pattern: {pattern2}")
    print(f"Matches tại: {matches2}")
    
    # Ví dụ 3
    print("\n" + "=" * 50)
    print("Ví dụ 3: Ma trận lớn hơn")
    text3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    pattern3 = [
        [6, 7],
        [10, 11]
    ]
    
    print("Text matrix (4x4):")
    for row in text3:
        print(f"  {row}")
    
    print("\nPattern matrix (2x2):")
    for row in pattern3:
        print(f"  {row}")
    
    matches3 = matrix_rolling_hash(text3, pattern3)
    print(f"\nMatches tại: {matches3}")
    
    print("\n--- PHÂN TÍCH ---")
    print("Rolling Hash 2D:")
    print("  + Tìm pattern trong ma trận trong O((r-p_r)(c-p_c))")
    print("  + Cải tiến: lợi dụng rolling hash để tính O(1)")
    print("  - Cần kiểm tra false positive (match hash không match thật)")
