def can_bac_hai_nguyen(x):
    left = 0
    right = x
    ans = 0

    while left <= right:
        mid = (left + right)// 2

        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
x = int(input("nhap x:"))
print(f"ket qua la:{can_bac_hai_nguyen(x)}")
            

