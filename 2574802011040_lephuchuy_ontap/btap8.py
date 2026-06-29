def bubble_sort_optimized_passes(a):
    arr = a.copy()
    n = len(arr)
    passes = 0
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        passes += 1
        if not swapped:
            break
    return arr, passes


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    sorted_arr, passes = bubble_sort_optimized_passes(a)
    print(sorted_arr, passes)
