def lower_bound(a, x):
    left = 0
    right = len(a)

    while left < right:
        mid = (left + right) // 2

        if a[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left


a = [1, 3, 5, 7]
x = 4

print(f"ket qua:{lower_bound(a, x)}")