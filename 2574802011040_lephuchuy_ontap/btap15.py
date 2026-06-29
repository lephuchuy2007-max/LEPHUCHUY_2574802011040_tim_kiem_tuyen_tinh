import heapq


def dijkstra(adj, src):
    n = len(adj)
    dist = [float('inf')] * n
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
                heapq.heappush(pq, (nd, v))
    return dist


if __name__ == '__main__':
    adj = [
        [(1, 2), (2, 5)],
        [(2, 1)],
        []
    ]
    print(dijkstra(adj, 0))
