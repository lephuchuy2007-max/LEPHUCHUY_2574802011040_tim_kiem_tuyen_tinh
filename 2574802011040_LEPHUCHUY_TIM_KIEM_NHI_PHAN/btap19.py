def aggressive_cows(x, c):
    x.sort()

    def can(dist):
        count = 1
        last = x[0]

        for i in range(1, len(x)):
            if x[i] - last >= dist:
                count += 1
                last = x[i]

        return count >= c

    left, right = 1, x[-1] - x[0]

    while left < right:
        mid = (left + right + 1) // 2
        if can(mid):
            left = mid
        else:
            right = mid - 1

    return left

print(aggressive_cows([1,2,4,8,9], 3))
