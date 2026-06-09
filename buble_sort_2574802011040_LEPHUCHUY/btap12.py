# btap12.py

def bubble_sort_string_length(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(a[j]) > len(a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    a = ['abc', 'a', 'ab']
    print("Sắp xếp theo độ dài chuỗi:", bubble_sort_string_length(a))  # Kết quả: ['a', 'ab', 'abc']