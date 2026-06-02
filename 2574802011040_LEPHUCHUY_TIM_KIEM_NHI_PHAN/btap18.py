def find_kth_positive(a, k):
    left, right = 0, len(a)-1

    while left <= right:
        mid = (left + right) // 2
        missing = a[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    return left + k

print(find_kth_positive([2,3,4,7,11], 5))
