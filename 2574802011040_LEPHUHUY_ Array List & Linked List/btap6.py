"""
Bài 6: Tự động mở rộng dung lượng (đã tích hợp trong btap1)
"""
from btap1 import ArrayList

if __name__ == '__main__':
    a = ArrayList(2)
    for i in range(6):
        a.add(i)
    print(a)
    print('capacity doubled when needed')