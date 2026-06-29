def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for x in num_set:
        if x - 1 not in num_set:
            curr = x
            length = 1
            while curr + 1 in num_set:
                curr += 1
                length += 1
            longest = max(longest, length)
    return longest


if __name__ == '__main__':
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
