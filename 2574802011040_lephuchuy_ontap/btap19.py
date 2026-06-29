import heapq


def shortest_path_grid(grid):
    n = len(grid)
    m = len(grid[0])
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while pq:
        d, x, y = heapq.heappop(pq)
        if d > dist[x][y]:
            continue
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                nd = d + grid[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    heapq.heappush(pq, (nd, nx, ny))
    return dist[n - 1][m - 1]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(shortest_path_grid(grid))
