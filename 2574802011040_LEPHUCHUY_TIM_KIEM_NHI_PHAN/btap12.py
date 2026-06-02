def Peak_Element(a):
    left = 0
    right =  len(a) - 1
    
    while left < right:
        mid = (left + right) // 2

        if a[mid] < a[mid + 1]:
            left  = mid + 1
        else:
            right = mid
    return left
a = [1, 2, 3, 1] 
print(f"ket qua:{Peak_Element(a)}")