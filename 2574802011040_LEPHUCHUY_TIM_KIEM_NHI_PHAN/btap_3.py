def phantutrung_min(a,x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
a =[1, 2, 2, 2, 3]
x = int(input("nhap:"))
print(f"ket qua la:{phantutrung_min(a,x)}")

    
    

