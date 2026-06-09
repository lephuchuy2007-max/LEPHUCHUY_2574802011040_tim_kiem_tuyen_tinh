# btap14.py
def cocktail_shaker_sort(a):
    n = len(a)
    start = 0
    end = n - 1
    swapped = True
    passes = 0
    while swapped:
        swapped = False
        passes += 1
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped:
            break
        end -= 1
        swapped = False
        for i in range(end - 1, start - 1, -1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        start += 1
    return a, passes

if __name__ == "__main__":
    a = [5, 1, 4, 2, 8]
    sorted_a, p = cocktail_shaker_sort(a)
    print(f"Mảng đã xếp: {sorted_a}, Số lượt: {p}")