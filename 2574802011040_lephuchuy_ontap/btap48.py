def rabin_karp(text, pattern, p=31, m=10**9+7):
    n, k = len(text), len(pattern)
    if k > n:
        return -1
    target_hash = 0
    text_hash = 0
    power = 1
    for i in range(k):
        target_hash = (target_hash * p + ord(pattern[i])) % m
        text_hash = (text_hash * p + ord(text[i])) % m
        if i:
            power = (power * p) % m
    for i in range(n - k + 1):
        if text_hash == target_hash:
            if text[i:i+k] == pattern:
                return i
        if i < n - k:
            text_hash = (text_hash - ord(text[i]) * power) % m
            text_hash = (text_hash * p + ord(text[i+k])) % m
            text_hash = (text_hash + m) % m
    return -1


if __name__ == '__main__':
    print(rabin_karp('zabcd', 'abc'))
