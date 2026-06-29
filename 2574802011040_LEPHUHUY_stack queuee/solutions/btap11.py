"""Bài 11: Next Greater Element (sử dụng stack đơn điệu)
"""

def next_greater(arr):
    n = len(arr)
    res = [-1]*n
    stack = []  # store indices
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            res[idx] = arr[i]
        stack.append(i)
    return res

if __name__ == '__main__':
    print(next_greater([2,1,3]))  # [3,3,-1]
