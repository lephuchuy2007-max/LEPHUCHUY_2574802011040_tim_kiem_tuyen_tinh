# btap5.py

def count_comparisons(a):
    n = len(a)
    comp_count = 0
    for i in range(n):
        for j in range(0, n - 1):
            comp_count += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return comp_count

if __name__ == "__main__":
    a = [1, 2, 3]
    print(f"Tổng số lần so sánh (chưa tối ưu): {count_comparisons(a)} lần")  # Kết quả: 3 lần