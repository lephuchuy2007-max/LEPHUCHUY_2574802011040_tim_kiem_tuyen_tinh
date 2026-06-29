"""Bài 4: Phát hiện underflow / overflow (đã bao gồm trong btap1)
- pop khi rỗng -> IndexError
- push khi đầy -> OverflowError
"""

from btap1 import StackArray


if __name__ == '__main__':
    s = StackArray(2)
    s.push(1)
    s.push(2)
    try:
        s.push(3)
    except OverflowError as e:
        print('overflow detected')
    s.pop(); s.pop()
    try:
        s.pop()
    except IndexError:
        print('underflow detected')
