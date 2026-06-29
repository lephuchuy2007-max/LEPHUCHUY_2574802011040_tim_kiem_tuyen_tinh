def two_sum(nums, target):
    comp = {}
    for i, x in enumerate(nums):
        if x in comp:
            return comp[x], i
        comp[target - x] = i
    return None


if __name__ == '__main__':
    print(two_sum([2, 7, 11], 9))
