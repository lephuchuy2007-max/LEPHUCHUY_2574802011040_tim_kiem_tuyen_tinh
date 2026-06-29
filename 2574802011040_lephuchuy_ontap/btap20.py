# Bài 20: So sánh Dijkstra, Bellman-Ford, A*
# Dijkstra: cạnh không âm, O((V+E) log V) với heap.
# Bellman-Ford: có cạnh âm, O(VE).
# A*: dùng heuristic admissible để dẫn đường nhanh hơn, áp dụng với đồ thị ô vuông hoặc không gian trạng thái.


def compare_algorithms():
    return {
        'Dijkstra': 'cạnh không âm, O((V+E) log V)',
        'Bellman-Ford': 'có cạnh âm được, O(VE)',
        'A*': 'heuristic hợp lệ, tìm nhanh hơn nếu heuristic tốt'
    }


if __name__ == '__main__':
    print(compare_algorithms())
