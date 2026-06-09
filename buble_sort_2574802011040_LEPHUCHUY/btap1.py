# btap1.py

def bubble_sort_one_pass(a):
    # Duyệt từ trái sang phải, hoán đổi cặp liền kề nếu sai thứ tự tăng dần
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            # Tiến hành hoán đổi (swap) hai giá trị liền kề
            a[i], a[i+1] = a[i+1], a[i]
    return a

if __name__ == "__main__":
    # Ví dụ mẫu theo đề bài bài 1
    a = [5, 1, 4, 2, 8]
    print("Mảng đầu vào: ", [5, 1, 4, 2, 8])
    
    ket_qua = bubble_sort_one_pass(a)
    print("Mảng sau 1 lượt:", ket_qua)  # Kết quả mong muốn: [1, 4, 2, 5, 8]