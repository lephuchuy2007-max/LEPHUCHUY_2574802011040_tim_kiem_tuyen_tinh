def tim_vi_tri_cuoi(a, x):
    vi_tri = -1

    for i in range(len(a)):
        if a[i] == x:
            vi_tri = i

    return vi_tri


a = [1, 2, 2, 2, 3]
x = 2

print(f"vitri:{tim_vi_tri_cuoi(a,x)}")
