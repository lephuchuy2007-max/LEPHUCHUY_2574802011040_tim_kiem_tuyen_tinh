# btap23.py

def analyze_bubble_sort(a):
    n = len(a)
    comparisons, swaps = 0, 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comparisons, swaps

if __name__ == "__main__":
    n = 10
    sorted_case = list(range(n))
    reverse_case = list(range(n, 0, -1))
    print(f"Đã sắp xếp | {analyze_bubble_sort(sorted_case)}")
    print(f"Ngược lại  | {analyze_bubble_sort(reverse_case)}")