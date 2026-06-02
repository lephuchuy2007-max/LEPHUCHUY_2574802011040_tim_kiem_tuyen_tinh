def vi_tri_chen(a, x):
    left = 0
    right = len(a) -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left
a = [ 1 , 3 , 5 ,6]
x = int(input("nhap:"))

print(f"ket qua la:{vi_tri_chen(a,x)}")
