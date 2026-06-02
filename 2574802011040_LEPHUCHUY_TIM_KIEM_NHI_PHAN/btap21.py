def split_array(nums, k):
    def can(limit):
        parts = 1
        cur = 0

        for x in nums:
            if cur + x <= limit:
                cur += x
            else:
                parts += 1
                cur = x

        return parts <= k

    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2

        if can(mid):
            right = mid
        else:
            left = mid + 1

    return left

print(split_array([7,2,5,10,8], 2))
