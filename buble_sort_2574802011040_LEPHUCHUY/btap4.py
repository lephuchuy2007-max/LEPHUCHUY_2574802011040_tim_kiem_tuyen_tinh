def count_swaps(a):
    n = len(a)
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swap_count += 1
    return swap_count

if __name__ == "__main__":
    a = [3, 2, 1]
    print(f"Tổng số lần hoán đổi: {count_swaps(a)} lần")  # Kết quả: 3 lần