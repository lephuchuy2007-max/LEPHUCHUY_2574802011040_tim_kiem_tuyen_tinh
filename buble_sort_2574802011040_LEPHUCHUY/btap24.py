# btap24.py

def min_passes_between_states(initial, current):
    passes = 0
    n = len(initial)
    temp = list(initial)
    while temp != current and passes < n:
        for j in range(0, n - 1):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]
        passes += 1
        if temp == current:
            break
    return passes

if __name__ == "__main__":
    dau = [4, 3, 2, 1]
    sau = [3, 2, 1, 4]
    print(f"Số lượt tối thiểu giữa 2 trạng thái: {min_passes_between_states(dau, sau)}")