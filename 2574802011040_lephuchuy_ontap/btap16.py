import heapq


def dijkstra_with_parent(adj, src):
    n = len(adj)
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent


def reconstruct_path(parent, t):
    path = []
    while t != -1:
        path.append(t)
        t = parent[t]
    return path[::-1]


if __name__ == '__main__':
    adj = [
        [(1, 1), (2, 4)],
        [(2, 2), (3, 5)],
        [(3, 1)],
        [(4, 3)],
        []
    ]
    dist, parent = dijkstra_with_parent(adj, 0)
    print(dist)
    print(reconstruct_path(parent, 4))
