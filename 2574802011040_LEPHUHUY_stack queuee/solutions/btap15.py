"""Bài 15: Sắp xếp một ngăn xếp (lớn nhất ở đỉnh)
Chỉ dùng 1 stack phụ và các phép so sánh
"""

def sort_stack(stack):
    temp = []
    while stack:
        cur = stack.pop()
        while temp and temp[-1] < cur:
            stack.append(temp.pop())
        temp.append(cur)
    # now temp has sorted descending (largest first). move back to stack so top is smallest if desired
    while temp:
        stack.append(temp.pop())
    return stack

if __name__ == '__main__':
    s = [3,1,2]
    print(sort_stack(s))  # [3,2,1] with top at end
