"""
Bài 4. Hai mảng có phần tử chung
Cho hai mảng, kiểm tra (và liệt kê) các phần tử xuất hiện ở cả hai
Dùng tập băm O(n)
"""

def common_elements(arr1, arr2):
    """Tìm phần tử chung giữa hai mảng"""
    set1 = set(arr1)
    common = set(arr2) & set1
    return sorted(common)


if __name__ == "__main__":
    # Ví dụ 1
    a1 = [1, 2, 3]
    a2 = [2, 3, 4]
    print(f"Mảng 1: {a1}")
    print(f"Mảng 2: {a2}")
    print(f"Phần tử chung: {common_elements(a1, a2)}")
    # Output: [2, 3]
    
    # Ví dụ 2
    a3 = ['a', 'b', 'c', 'd']
    a4 = ['b', 'd', 'e', 'f']
    print(f"\nMảy 1: {a3}")
    print(f"Mảy 2: {a4}")
    print(f"Phần tử chung: {common_elements(a3, a4)}")
    # Output: ['b', 'd']
    
    # Ví dụ 3 - Không có phần tử chung
    a5 = [1, 2, 3]
    a6 = [4, 5, 6]
    print(f"\nMảy 1: {a5}")
    print(f"Mảy 2: {a6}")
    print(f"Phần tử chung: {common_elements(a5, a6)}")
    # Output: []
