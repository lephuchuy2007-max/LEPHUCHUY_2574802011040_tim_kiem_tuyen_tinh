"""Bài 11: Giá trị lớn nhất trong cửa sổ trượt (deque đơn điệu)
"""
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k-1:
            res.append(nums[dq[0]])
    return res

if __name__ == '__main__':
    print(max_sliding_window([1,3,-1,-3,5,3], 3))  # [3,3,5,5]
