def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        hours = sum((p + mid - 1)//mid for p in piles)
        if hours <= h:
            right = mid
        else:
            left = mid + 1
    return left

print(min_eating_speed([3,6,7,11], 8))
