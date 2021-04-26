#BFS (Shortest path and Search)
from collections import deque
def bfs(start,graph):
    explored = set()
    queue = deque([start])
    levels = {}
    levels[start]= 0
    visited = {start}
    while queue:
        node = queue.popleft()
        explored.add(node)
        if node not in graph:
            continue

        neighbours = graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                levels[neighbour]= levels[node]+1

    return levels


# DFS (Iterative)
def dfs(x, graph):
    stack = [x]
    visited = set()
    while len(stack) > 0:
        node = stack.pop()
        visited.add(node)
        if node not in graph:
            continue

        for i in graph[node]:
            if i not in visited:
                stack.append(i)

    return visited