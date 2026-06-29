# Bài 12: Ổn định của bubble/insertion/selection
# Bubble sort và insertion sort ổn định, selection sort không ổn định.
# Ví dụ selection sort sửa thứ tự của phần tử bằng giá trị bằng.


def selection_sort_is_stable_example(a):
    arr = a.copy()
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == '__main__':
    a = [(2, 'a'), (1, 'a'), (2, 'b')]
    print(selection_sort_is_stable_example(a))
