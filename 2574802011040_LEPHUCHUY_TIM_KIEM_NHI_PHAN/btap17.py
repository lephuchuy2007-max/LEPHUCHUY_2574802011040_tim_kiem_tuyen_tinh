def ship_within_days(weights, D):
    def can(cap):
        days = 1
        cur = 0
        for w in weights:
            if cur + w <= cap:
                cur += w
            else:
                days += 1
                cur = w
        return days <= D

    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2
        if can(mid):
            right = mid
        else:
            left = mid + 1
    return left

print(ship_within_days([1,2,3,4,5,6,7,8,9,10], 5))
