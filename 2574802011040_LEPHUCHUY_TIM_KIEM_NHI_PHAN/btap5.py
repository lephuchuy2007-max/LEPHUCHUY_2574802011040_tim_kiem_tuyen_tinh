def solanxuathien(a,x):
    dem = 0
    for i in range(len(a)):
        if a[i] == x:
            dem += 1
    return dem
a =  [1, 2, 2, 2, 3]
x = int(input("nhap:"))
print(f"so lan x xuat hien trong list la {solanxuathien(a,x)}")