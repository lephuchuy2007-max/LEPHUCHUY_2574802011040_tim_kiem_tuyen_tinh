def polynomial_hash(s, p=31, m=10**9+7):
    h = 0
    power = 1
    for ch in s:
        h = (h + (ord(ch) - ord('a') + 1) * power) % m
        power = (power * p) % m
    return h


if __name__ == '__main__':
    print(polynomial_hash('abc'))
