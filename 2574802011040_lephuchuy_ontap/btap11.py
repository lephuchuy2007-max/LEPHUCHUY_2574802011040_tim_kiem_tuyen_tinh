def selection_sort_count_comparisons(a):
    arr = a.copy()
    n = len(arr)
    comparisons = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, comparisons


if __name__ == '__main__':
    a = [2, 1, 4, 3, 5]
    sorted_arr, comparisons = selection_sort_count_comparisons(a)
    print(sorted_arr, comparisons)
