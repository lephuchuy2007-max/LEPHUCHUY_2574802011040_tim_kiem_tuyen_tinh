"""Bài 12: Hình chữ nhật lớn nhất trong histogram
O(n) stack
"""

def largest_rectangle(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            H = heights[stack.pop()]
            L = stack[-1] if stack else -1
            max_area = max(max_area, H * (i - L - 1))
        stack.append(i)
    return max_area

if __name__ == '__main__':
    print(largest_rectangle([2,1,5,6,2,3]))  # 10
