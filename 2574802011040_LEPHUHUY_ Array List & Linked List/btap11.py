"""
Bài 11: Xoay mảng k vị trí (rotate right k) bằng 3 lần reverse
"""
def reverse_range(arr, i, j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1; j-=1

def rotate_right(arr, k):
    n=len(arr)
    if n==0: return arr
    k %= n
    reverse_range(arr,0,n-1)
    reverse_range(arr,0,k-1)
    reverse_range(arr,k,n-1)
    return arr

if __name__ == '__main__':
    print(rotate_right([1,2,3,4,5],2))