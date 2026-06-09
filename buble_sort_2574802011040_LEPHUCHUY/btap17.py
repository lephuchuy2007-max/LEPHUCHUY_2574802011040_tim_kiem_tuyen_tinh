# btap17.py

def bubble_sort_partial(a, k):
    n = len(a)
    for i in range(k):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    a = [3, 1, 4, 1, 5]
    k = 2
    print("Mảng sau k lượt:", bubble_sort_partial(a, k))