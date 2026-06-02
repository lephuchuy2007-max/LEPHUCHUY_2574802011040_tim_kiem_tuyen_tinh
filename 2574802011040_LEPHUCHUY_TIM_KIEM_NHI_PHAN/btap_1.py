def tim_kiem(a,x):
    for i in range (len(a)):
        if a[i] == x:
            return i
    return -1
a = [1, 3, 5, 7, 9]
x = 7
print(f"x duoc tim thay tai vi tri so:{tim_kiem(a,x)} trong list")