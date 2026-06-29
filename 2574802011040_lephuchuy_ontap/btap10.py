def binary_insertion_sort(a):
    arr = a.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        left = 0
        right = i
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key
    return arr


if __name__ == '__main__':
    a = [3, 2, 1]
    print(binary_insertion_sort(a))
