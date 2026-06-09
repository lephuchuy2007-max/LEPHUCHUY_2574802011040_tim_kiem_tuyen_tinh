# btap22.py

def bubble_sort_k_bounded(a, k):
    n = len(a)
    passes = 0
    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped or passes > k: 
            break
    return a, passes

if __name__ == "__main__":
    a = [2, 1, 4, 3, 6, 5]
    sorted_a, p = bubble_sort_k_bounded(a, 1)
    print(f"Kết quả mảng: {sorted_a}, Số lượt: {p}")