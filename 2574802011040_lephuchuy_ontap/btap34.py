def remove_duplicates_keep_order(a):
    seen = set()
    result = []
    for x in a:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


if __name__ == '__main__':
    print(remove_duplicates_keep_order([3, 1, 3, 2, 1]))
