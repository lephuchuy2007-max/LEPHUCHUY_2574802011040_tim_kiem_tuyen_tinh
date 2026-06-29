"""
Bài 9. Two Sum dùng hash
Tìm hai chỉ số có a[i] + a[j] = target trong O(n) bằng bảng băm lưu phần bù
"""

def two_sum(nums, target):
    """
    Tìm hai chỉ số i, j sao cho nums[i] + nums[j] = target
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


if __name__ == "__main__":
    # Ví dụ 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Array: {nums1}")
    print(f"Target: {target1}")
    print(f"Kết quả: {result1}")
    print(f"Kiểm tra: {nums1[result1[0]]} + {nums1[result1[1]]} = {nums1[result1[0]] + nums1[result1[1]]}")
    # Output: (0, 1) vì 2 + 7 = 9
    
    # Ví dụ 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"\nArray: {nums2}")
    print(f"Target: {target2}")
    print(f"Kết quả: {result2}")
    print(f"Kiểm tra: {nums2[result2[0]]} + {nums2[result2[1]]} = {nums2[result2[0]] + nums2[result2[1]]}")
    # Output: (1, 2) vì 2 + 4 = 6
    
    # Ví dụ 3 - Không có lời giải
    nums3 = [1, 2, 3]
    target3 = 10
    result3 = two_sum(nums3, target3)
    print(f"\nArray: {nums3}")
    print(f"Target: {target3}")
    print(f"Kết quả: {result3}")
