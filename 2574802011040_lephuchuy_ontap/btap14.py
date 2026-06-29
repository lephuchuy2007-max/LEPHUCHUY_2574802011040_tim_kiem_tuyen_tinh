def shell_sort(a, gaps=None):
    arr = a.copy()
    n = len(arr)
    if gaps is None:
        gaps = [n // 2, n // 4, 1]
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr


if __name__ == '__main__':
    a = [8, 5, 3, 7, 2, 6, 4, 1]
    print(shell_sort(a, gaps=[4, 2, 1]))
