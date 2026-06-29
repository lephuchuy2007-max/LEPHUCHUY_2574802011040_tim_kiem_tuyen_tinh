"""
Bài 3. Đếm tần suất
Dùng bảng băm đếm số lần xuất hiện của mỗi phần tử trong một mảng
"""

def count_frequency(arr):
    """Đếm tần suất xuất hiện của mỗi phần tử"""
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq


if __name__ == "__main__":
    # Ví dụ 1
    arr1 = ['a', 'b', 'a', 'c', 'a']
    print("Mảng:", arr1)
    print("Tần suất:", count_frequency(arr1))
    # Output: {'a': 3, 'b': 1, 'c': 1}
    
    # Ví dụ 2
    arr2 = [1, 1, 1, 2, 2, 3]
    print("\nMảng:", arr2)
    print("Tần suất:", count_frequency(arr2))
    # Output: {1: 3, 2: 2, 3: 1}
    
    # Ví dụ 3
    arr3 = 'leetcode'
    print("\nChuỗi:", arr3)
    print("Tần suất:", count_frequency(arr3))
    # Output: {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}
