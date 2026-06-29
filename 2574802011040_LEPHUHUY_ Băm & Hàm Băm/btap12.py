"""
Bài 12. Tổng đoạn con bằng k
Đếm số đoạn con liên tiếp có tổng bằng k, dùng tổng tiền tố + bảng băm trong O(n)
"""

def subarray_sum_equal_k(nums, k):
    """
    Đếm số đoạn con liên tiếp có tổng bằng k
    Dùng tổng tiền tố (prefix sum)
    """
    prefix_sum = 0
    seen = {0: 1}  # {tổng tiền tố: số lần xuất hiện}
    count = 0
    
    for num in nums:
        prefix_sum += num
        
        # Kiểm tra xem (prefix_sum - k) đã xuất hiện chưa
        # Nếu có, tức là có đoạn con từ vị trí cũ đến hiện tại có tổng = k
        count += seen.get(prefix_sum - k, 0)
        
        # Lưu tổng tiền tố hiện tại
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    
    return count


if __name__ == "__main__":
    # Ví dụ 1
    nums1 = [1, 1, 1]
    k1 = 2
    result1 = subarray_sum_equal_k(nums1, k1)
    print(f"Array: {nums1}")
    print(f"k: {k1}")
    print(f"Kết quả: {result1}")
    print(f"Giải thích: [1,1] (chỉ số 0-1) và [1,1] (chỉ số 1-2)")
    # Output: 2
    
    # Ví dụ 2
    nums2 = [1, 2, 1, 2, 1]
    k2 = 3
    result2 = subarray_sum_equal_k(nums2, k2)
    print(f"\nArray: {nums2}")
    print(f"k: {k2}")
    print(f"Kết quả: {result2}")
    # Output: 2
    # [1,2] (0-1) và [2,1] (1-2)
    
    # Ví dụ 3
    nums3 = [1, -1, 1, 1]
    k3 = 1
    result3 = subarray_sum_equal_k(nums3, k3)
    print(f"\nArray: {nums3}")
    print(f"k: {k3}")
    print(f"Kết quả: {result3}")
    # Output: 2
    # [1, -1, 1] (0-2) và [1] (2) và [1] (3)
