# btap20.py

def merge_and_count(arr, temp_arr, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
    return inv_count

def merge_sort_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count

def count_swaps_fast(a):
    temp_arr = [0]*len(a)
    return merge_sort_count(a, temp_arr, 0, len(a) - 1)

if __name__ == "__main__":
    a = [2, 3, 1]
    print(f"Số swap đếm nhanh O(n log n): {count_swaps_fast(a)}")