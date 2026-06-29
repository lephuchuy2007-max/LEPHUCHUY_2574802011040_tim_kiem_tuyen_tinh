def insertion_sort_count_shifts(a):
    arr = a.copy()
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        arr[j + 1] = key
    return arr, shifts


if __name__ == '__main__':
    a = [3, 2, 1]
    sorted_arr, shifts = insertion_sort_count_shifts(a)
    print(sorted_arr, shifts)
