def rotate_array(a, k):
    n = len(a)
    k %= n
    def reverse(sub):
        i, j = 0, len(sub) - 1
        while i < j:
            sub[i], sub[j] = sub[j], sub[i]
            i += 1
            j -= 1
    reverse(a)
    reverse(a[:k])
    reverse(a[k:])
    return a


if __name__ == '__main__':
    print(rotate_array([1, 2, 3, 4, 5], 2))
