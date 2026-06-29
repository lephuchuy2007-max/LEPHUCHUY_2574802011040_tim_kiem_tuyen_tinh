def min_eating_speed(piles, h):
    def can_finish(k):
        total = 0
        for pile in piles:
            total += (pile + k - 1) // k
        return total <= h

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    piles = [3, 6, 7, 11]
    h = 8
    print(min_eating_speed(piles, h))
