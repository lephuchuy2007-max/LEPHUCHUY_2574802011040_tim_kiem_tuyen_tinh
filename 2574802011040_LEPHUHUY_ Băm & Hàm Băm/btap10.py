"""
Bài 10. Phần tử không lặp đầu tiên
Tìm phần tử đầu tiên không bị lặp trong một dãy
"""

def first_unique_char(s):
    """
    Tìm ký tự đầu tiên xuất hiện đúng một lần
    """
    freq = {}
    
    # Đếm tần suất từng ký tự
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # Tìm ký tự đầu tiên có tần suất = 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    
    return None


if __name__ == "__main__":
    # Ví dụ 1
    s1 = 'leetcode'
    result1 = first_unique_char(s1)
    print(f"Chuỗi: '{s1}'")
    print(f"Ký tự không lặp đầu tiên: '{result1}'")
    # Output: 'l'
    
    # Ví dụ 2
    s2 = 'loveleetcode'
    result2 = first_unique_char(s2)
    print(f"\nChuỗi: '{s2}'")
    print(f"Ký tự không lặp đầu tiên: '{result2}'")
    # Output: 'v'
    
    # Ví dụ 3
    s3 = 'aabb'
    result3 = first_unique_char(s3)
    print(f"\nChuỗi: '{s3}'")
    print(f"Ký tự không lặp đầu tiên: {result3}")
    # Output: None
    
    # Ví dụ 4
    s4 = 'aabcdddeeeeaabcd'
    result4 = first_unique_char(s4)
    print(f"\nChuỗi: '{s4}'")
    print(f"Ký tự không lặp đầu tiên: '{result4}'")
    # Output: 'b'
