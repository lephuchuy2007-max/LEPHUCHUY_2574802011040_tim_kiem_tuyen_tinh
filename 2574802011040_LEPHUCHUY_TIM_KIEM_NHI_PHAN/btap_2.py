def tim_kiem_ton_tai(a,x):   
    if x in a:
        return True
    else:
        return False
    
a = [2, 4, 6, 8]
x = int(input("nhap so can tim:"))
print(tim_kiem_ton_tai(a,x))



