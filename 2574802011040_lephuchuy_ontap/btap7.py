def bubble_sort_count_swaps(a):
    arr = a.copy()
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, swaps


if __name__ == '__main__':
    a = [2, 3, 1]
    sorted_arr, swaps = bubble_sort_count_swaps(a)
    print(sorted_arr, swaps)
