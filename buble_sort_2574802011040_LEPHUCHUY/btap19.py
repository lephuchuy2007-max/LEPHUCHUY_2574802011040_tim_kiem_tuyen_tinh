# btap19.py

def min_passes_analysis(a):
    n = len(a)
    max_backward_dist = 0
    sorted_a = sorted(a)
    pos_map = {val: idx for idx, val in enumerate(sorted_a)}
    for current_idx, val in enumerate(a):
        correct_idx = pos_map[val]
        backward_dist = current_idx - correct_idx
        if backward_dist > max_backward_dist:
            max_backward_dist = backward_dist
    return max(1, max_backward_dist)

if __name__ == "__main__":
    a = [1, 2, 3, 5, 4]
    print(f"Số lượt tối thiểu: {min_passes_analysis(a)}")