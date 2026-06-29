from collections import deque


def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []
    dq = deque()
    res = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res


if __name__ == '__main__':
    print(max_sliding_window([1, 3, -1, -3, 5, 3], 3))
