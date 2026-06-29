def count_inversions(arr):
    def merge_count(left, right):
        merged = []
        i = j = inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    def sort_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_left = sort_count(a[:mid])
        right, inv_right = sort_count(a[mid:])
        merged, inv_split = merge_count(left, right)
        return merged, inv_left + inv_right + inv_split

    _, inv = sort_count(arr)
    return inv


if __name__ == '__main__':
    a = [3, 1, 2]
    print(count_inversions(a))
