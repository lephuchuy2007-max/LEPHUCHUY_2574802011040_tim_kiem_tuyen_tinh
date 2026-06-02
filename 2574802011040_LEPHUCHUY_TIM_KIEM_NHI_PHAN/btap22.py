def find_median_sorted_arrays(a, b):
    if len(a) > len(b):
        a, b = b, a

    m, n = len(a), len(b)
    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        maxL1 = float("-inf") if i == 0 else a[i-1]
        minR1 = float("inf") if i == m else a[i]

        maxL2 = float("-inf") if j == 0 else b[j-1]
        minR2 = float("inf") if j == n else b[j]

        if maxL1 <= minR2 and maxL2 <= minR1:
            if (m+n) % 2 == 0:
                return (max(maxL1,maxL2)+min(minR1,minR2))/2
            return max(maxL1,maxL2)

        elif maxL1 > minR2:
            right = i - 1
        else:
            left = i + 1

print(find_median_sorted_arrays([1,2],[3,4]))
