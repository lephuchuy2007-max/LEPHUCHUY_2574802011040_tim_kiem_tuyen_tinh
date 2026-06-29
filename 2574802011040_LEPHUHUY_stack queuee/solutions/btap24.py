"""Bài 9: BFS dùng hàng đợi
"""
from collections import deque

def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order

if __name__ == '__main__':
    g = {1:[2,3],2:[4],3:[],4:[]}
    print(bfs(g,1))
