"""
Bài 5. Nhóm theo khóa (group by)
Nhóm các phần tử theo một khóa dẫn xuất, dùng bảng băm ánh xạ khóa → danh sách
"""

def group_by(items, key_func):
    """Nhóm các phần tử theo hàm tạo khóa"""
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups


if __name__ == "__main__":
    # Ví dụ 1: Nhóm từ theo chữ cái đầu
    words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
    result = group_by(words, lambda w: w[0])
    print("Nhóm từ theo chữ cái đầu:")
    for key in sorted(result):
        print(f"  '{key}': {result[key]}")
    # Output:
    # 'a': ['apple', 'apricot']
    # 'b': ['banana', 'blueberry']
    # 'c': ['cherry']
    
    # Ví dụ 2: Nhóm số theo số dư khi chia 2
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result2 = group_by(numbers, lambda n: n % 2)
    print("\nNhóm số theo chẵn/lẻ:")
    for key in sorted(result2):
        print(f"  {key}: {result2[key]}")
    # Output:
    # 0: [2, 4, 6, 8, 10]
    # 1: [1, 3, 5, 7, 9]
    
    # Ví dụ 3: Nhóm theo độ dài từ
    result3 = group_by(words, len)
    print("\nNhóm từ theo độ dài:")
    for key in sorted(result3):
        print(f"  {key}: {result3[key]}")
