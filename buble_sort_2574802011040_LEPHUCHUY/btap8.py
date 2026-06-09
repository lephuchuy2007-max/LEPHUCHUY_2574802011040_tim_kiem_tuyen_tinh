# btap8.py

def is_sorted_after_k_passes(a, k):
    n = len(a)
    for i in range(min(k, n)):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
    for i in range(n - 1):
        if a[i] > a[i+1]:
            return False
    return True

if __name__ == "__main__":
    a = [3, 2, 1]
    k = 1
    print(f"Đã sắp xếp sau {k} lượt chưa:", is_sorted_after_k_passes(a, k))  # Kết quả: False