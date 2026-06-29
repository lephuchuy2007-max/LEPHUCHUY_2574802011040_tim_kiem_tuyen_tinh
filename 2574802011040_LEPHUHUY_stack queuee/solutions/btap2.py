"""Bài 2: Đảo ngược chuỗi dùng ngăn xếp
"""

from btap1 import StackArray


def reverse_string(s: str) -> str:
    st = StackArray(len(s))
    for ch in s:
        st.push(ch)
    res = []
    while not st.isEmpty():
        res.append(st.pop())
    return ''.join(res)


if __name__ == '__main__':
    print(reverse_string('abc'))  # cba
