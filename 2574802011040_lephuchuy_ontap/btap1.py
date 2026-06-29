# Bài tập 1: tìm chỉ số x trong mảng đã sắp xếp tăng dần bằng while, trả về -1 nếu không tìm thấy.
def timkiem(a, x):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    x = int(input('Nhap so can tim: '))
    print(timkiem(a, x))
a = [1, 3, 5, 7, 9]
x = int(input("nhap so can tim:"))
print(timkiem(a,x))
    



 

