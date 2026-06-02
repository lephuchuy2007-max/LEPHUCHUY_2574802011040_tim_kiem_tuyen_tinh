def tim_phan_tu_don_le(a):
    left = 0
    right = len(a) - 1
    
    
    while left < right:
        mid = (left + right) // 2
        

        if mid % 2 == 1:
            mid -= 1

        if a[mid] == a[mid + 1]:
            left = mid + 2
        else:
            right = mid
    
    return a[left]
a = [1, 1, 2, 3, 3, 4, 4]
print(f"ket qua:=:{tim_phan_tu_don_le(a)}")