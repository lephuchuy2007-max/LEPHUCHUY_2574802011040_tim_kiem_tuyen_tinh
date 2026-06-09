# btap11.py

def bubble_sort_absolute(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if abs(a[j]) > abs(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    a = [-3, 1, -2, 2]
    print("Sắp xếp theo trị tuyệt đối:", bubble_sort_absolute(a))  # Kết quả: [1, -2, 2, -3]