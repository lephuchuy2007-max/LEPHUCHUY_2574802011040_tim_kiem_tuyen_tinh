def bubble_sort_ascending(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    a = [5, 1, 4, 2, 8]
    print("Mảng tăng dần:", bubble_sort_ascending(a))  # Kết quả: [1, 2, 4, 5, 8]