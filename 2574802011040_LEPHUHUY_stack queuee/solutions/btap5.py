"""Bài 5: Duyệt và đếm phần tử mà không làm mất ngăn xếp
Sử dụng ngăn xếp phụ để khôi phục trạng thái
"""

from btap1 import StackArray


def elements_lifo(stack: StackArray):
    temp = StackArray(stack.capacity)
    result = []
    while not stack.isEmpty():
        val = stack.pop()
        result.append(val)
        temp.push(val)
    while not temp.isEmpty():
        stack.push(temp.pop())
    return result


if __name__ == '__main__':
    s = StackArray(10)
    for v in [1,2,3]: s.push(v)
    print(elements_lifo(s))  # [3,2,1]
    print(s.top())  # still 3
