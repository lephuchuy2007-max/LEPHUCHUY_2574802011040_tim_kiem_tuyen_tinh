def minmax_gas_dist(stations, k):
    def needed(d):
        count = 0
        for i in range(1, len(stations)):
            count += int((stations[i] - stations[i-1]) / d)
        return count

    left = 0.0
    right = stations[-1] - stations[0]

    for _ in range(100):
        mid = (left + right) / 2

        if needed(mid) > k:
            left = mid
        else:
            right = mid

    return right

print(minmax_gas_dist([1,2,3,4,5,6,7,8,9,10], 9))
