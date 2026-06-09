# btap1.py

def bubble_sort_one_pass(a):

    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
           
            a[i], a[i+1] = a[i+1], a[i]
    return a

if __name__ == "__main__":

    a = [5, 1, 4, 2, 8]
    print("Mảng đầu vào: ", [5, 1, 4, 2, 8])
    
    ket_qua = bubble_sort_one_pass(a)
    print("Mảng sau 1 lượt:", ket_qua) 
