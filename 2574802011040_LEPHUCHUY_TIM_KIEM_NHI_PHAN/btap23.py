def kth_smallest(matrix, k):
    n = len(matrix)

    def count_le(x):
        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= x:
                count += row + 1
                col += 1
            else:
                row -= 1

        return count

    left = matrix[0][0]
    right = matrix[-1][-1]

    while left < right:
        mid = (left + right) // 2

        if count_le(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left

print(kth_smallest([[1,5,9],[10,11,13],[12,13,15]], 8))
