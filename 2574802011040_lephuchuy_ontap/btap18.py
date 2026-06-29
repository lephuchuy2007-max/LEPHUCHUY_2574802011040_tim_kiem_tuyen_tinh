# Bài 18: Dijkstra cần cạnh không âm.
# Nếu đồ thị có cạnh âm, Dijkstra có thể chốt nhầm một đỉnh.
# Ví dụ: 0->1 (1), 0->2 (4), 1->2 (-3).
# Dijkstra từ 0 sẽ chọn 2 sau 1 mà bỏ sót đường 0->1->2.
# Thuật toán thay thế: Bellman-Ford.


def bellman_ford(edges, n, src):
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    return dist


if __name__ == '__main__':
    edges = [(0, 1, 1), (0, 2, 4), (1, 2, -3)]
    print(bellman_ford(edges, 3, 0))
