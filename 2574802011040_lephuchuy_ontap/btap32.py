def remove_if(a, predicate):
    write = 0
    for read in range(len(a)):
        if not predicate(a[read]):
            a[write] = a[read]
            write += 1
    return a[:write]


if __name__ == '__main__':
    print(remove_if([1, 2, 3, 4], lambda x: x % 2 == 0))
