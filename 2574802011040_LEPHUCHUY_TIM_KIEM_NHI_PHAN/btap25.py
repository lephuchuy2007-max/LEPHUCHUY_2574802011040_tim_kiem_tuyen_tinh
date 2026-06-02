def max_distance(position, m):
    position.sort()

    def can(dist):
        count = 1
        last = position[0]

        for x in position[1:]:
            if x - last >= dist:
                count += 1
                last = x

        return count >= m

    left = 1
    right = position[-1] - position[0]

    while left < right:
        mid = (left + right + 1) // 2

        if can(mid):
            left = mid
        else:
            right = mid - 1

    return left

print(max_distance([1,2,3,4,7], 3))
