def binary_search_for(a, x):
    """Bài tập 2: tìm chỉ số x trong mảng tăng dần bằng for và O(log n)."""
    left = 0
    right = len(a) - 1
    # Số lần lặp tối đa là bit_length của độ dài mảng
    for _ in range(len(a).bit_length()):
        if left > right:
            break
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    x = int(input('Nhap so can tim: '))
    print(binary_search_for(a, x))
