import heapq


def dijkstra_heap(adj, src):
    n = len(adj)
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]
    visited = [False] * n
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist


if __name__ == '__main__':
    adj = [
        [(1, 2), (2, 4)],
        [(2, 1), (3, 7)],
        [(4, 3)],
        [(4, 1)],
        []
    ]
    print(dijkstra_heap(adj, 0))
