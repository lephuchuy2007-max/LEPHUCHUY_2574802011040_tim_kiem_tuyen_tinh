# btap10.py

def count_total_passes(a):
    n = len(a)
    passes = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        passes += 1
        if not swapped:
            break
    return passes

if __name__ == "__main__":
    a = [2, 1, 3, 4]
    print(f"Số lượt cần thiết: {count_total_passes(a)} lượt")  # Kết quả: 2 lượt