def allocate_books(p, m):
    def can(limit):
        students = 1
        pages = 0

        for book in p:
            if pages + book <= limit:
                pages += book
            else:
                students += 1
                pages = book

        return students <= m

    left = max(p)
    right = sum(p)

    while left < right:
        mid = (left + right) // 2

        if can(mid):
            right = mid
        else:
            left = mid + 1

    return left

print(allocate_books([12,34,67,90], 2))
