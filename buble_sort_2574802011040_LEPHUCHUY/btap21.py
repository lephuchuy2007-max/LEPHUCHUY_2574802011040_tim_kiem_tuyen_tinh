# btap21.py

def stable_bubble_sort_kv(records):
    n = len(records)
    for i in range(n):
        for j in range(0, n - i - 1):
            if records[j][0] > records[j+1][0]:
                records[j], records[j+1] = records[j+1], records[j]
    return records

if __name__ == "__main__":
    data = [(1, "v1"), (2, "v2-first"), (2, "v2-second"), (0, "v0")]
    print("Mảng bản ghi ổn định:", stable_bubble_sort_kv(data))