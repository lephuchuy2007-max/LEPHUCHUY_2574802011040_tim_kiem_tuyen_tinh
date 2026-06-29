"""Bài 13: DFS iterative dùng stack
"""

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()
        if node in visited: continue
        visited.add(node)
        order.append(node)
        for nei in reversed(graph.get(node, [])):
            if nei not in visited:
                stack.append(nei)
    return order

if __name__ == '__main__':
    g = {1:[2,3],2:[4],3:[],4:[]}
    print(dfs_iterative(g,1))
