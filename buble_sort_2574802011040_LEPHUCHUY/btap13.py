# btap13.py

def verify_stability(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j][0] > a[j+1][0]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

if __name__ == "__main__":
    a = [(2, 'a'), (1, 'b'), (2, 'c')]
    print("Chứng minh tính ổn định:", verify_stability(a))  # Kết quả: [(1, 'b'), (2, 'a'), (2, 'c')]