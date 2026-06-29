import bisect

# Bài 3: lower_bound và upper_bound

def lower_bound(a, x):
    """Trả về chỉ số phần tử nhỏ nhất >= x, hoặc len(a) nếu không có."""
    return bisect.bisect_left(a, x)


def upper_bound(a, x):
    """Trả về chỉ số phần tử nhỏ nhất > x, hoặc len(a) nếu không có."""
    return bisect.bisect_right(a, x)


if __name__ == '__main__':
    a = [1, 3, 5, 7]
    x = 4
    print('lower =', lower_bound(a, x))
    print('upper =', upper_bound(a, x))
