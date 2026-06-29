from collections import deque


def bfs(adj, start):
    visited = [False] * len(adj)
    order = []
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return order


if __name__ == '__main__':
    adj = [[1, 2], [3], [3], []]
    print(bfs(adj, 0))
