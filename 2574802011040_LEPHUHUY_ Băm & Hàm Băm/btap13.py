"""
Bài 13. Dãy liên tiếp dài nhất
Tìm độ dài dãy số nguyên liên tiếp dài nhất trong một mảng (không cần kề nhau), trong O(n)
"""

def longest_consecutive(nums):
    """
    Tìm độ dài dãy số nguyên liên tiếp dài nhất
    Không yêu cầu các phần tử kề nhau
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    best = 0
    
    for num in num_set:
        # Chỉ bắt đầu từ phần tử bé nhất của mỗi dãy
        # (num-1 không tồn tại)
        if num - 1 not in num_set:
            length = 1
            # Đếm độ dài dãy liên tiếp
            while num + length in num_set:
                length += 1
            best = max(best, length)
    
    return best


if __name__ == "__main__":
    # Ví dụ 1
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = longest_consecutive(nums1)
    print(f"Array: {nums1}")
    print(f"Dãy liên tiếp dài nhất: {result1}")
    print(f"Giải thích: dãy [1,2,3,4] có độ dài 4")
    # Output: 4
    
    # Ví dụ 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    result2 = longest_consecutive(nums2)
    print(f"\nArray: {nums2}")
    print(f"Dãy liên tiếp dài nhất: {result2}")
    print(f"Giải thích: dãy [0,1,2,3,4,5,6,7,8] có độ dài 9")
    # Output: 9
    
    # Ví dụ 3
    nums3 = [9, 1,4, 7, 3,2,8,5, 6]
    result3 = longest_consecutive(nums3)
    print(f"\nArray: {nums3}")
    print(f"Dãy liên tiếp dài nhất: {result3}")
    print(f"Giải thích: dãy [1,2,3,4,5,6,7,8,9] có độ dài 9")
    # Output: 9
    
    # Ví dụ 4 - Mảng rỗng
    nums4 = []
    result4 = longest_consecutive(nums4)
    print(f"\nArray: {nums4}")
    print(f"Dãy liên tiếp dài nhất: {result4}")
    # Output: 0
