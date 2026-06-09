# btap6.py

def last_element_after_one_pass(a):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    return a[-1]

if __name__ == "__main__":
    a = [4, 2, 7, 1, 3]
    print("Giá trị nằm ở cuối sau 1 lượt:", last_element_after_one_pass(a))  # Kết quả: 7