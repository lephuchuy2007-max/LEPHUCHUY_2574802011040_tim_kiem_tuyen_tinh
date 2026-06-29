def split_array(nums, k):
    def can_split(max_sum):
        curr = 0
        parts = 1
        for x in nums:
            if curr + x > max_sum:
                parts += 1
                curr = x
            else:
                curr += x
        return parts <= k

    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    a = [7, 2, 5, 10, 8]
    print(split_array(a, 2))
