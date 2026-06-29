def subarray_sum_equals_k(nums, k):
    prefix_sum = 0
    counts = {0: 1}
    total = 0
    for x in nums:
        prefix_sum += x
        total += counts.get(prefix_sum - k, 0)
        counts[prefix_sum] = counts.get(prefix_sum, 0) + 1
    return total


if __name__ == '__main__':
    print(subarray_sum_equals_k([1, 1, 1], 2))
