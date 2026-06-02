def tim_x(a, x):
    m = len(a)
    n = len(a[0])

    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2

        row = mid // n
        col = mid % n

        if a[row][col] == x:
            return True

        elif a[row][col] < x:
            left = mid + 1

        else:
            right = mid - 1

    return False