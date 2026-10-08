# EXTRA (added): graph topics that were missing from graphs.py
# (add_edge is built here, DFS was missing, plus a few common problems)
from collections import deque

############# build an undirected graph (adjacency list) #############
graph = {}

def add_edge(u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

add_edge('A', 'B')
add_edge('A', 'C')
add_edge('A', 'E')
add_edge('B', 'C')
add_edge('B', 'D')
print(graph)


############# BFS (using deque - faster than list.pop(0)) #############
def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

print("BFS:")
bfs(graph, 'A')            # A B C E D
print()


############# DFS (recursive) #############
def dfs(graph, node, visited):
    visited.append(node)
    print(node, end=" ")
    for i in graph[node]:
        if i not in visited:
            dfs(graph, i, visited)

print("DFS (recursive):")
dfs(graph, 'A', [])        # A B C D E
print()


############# DFS (iterative, using a stack) #############
def dfs_iterative(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")
            for i in reversed(graph[node]):
                if i not in visited:
                    stack.append(i)

print("DFS (iterative):")
dfs_iterative(graph, 'A')  # A B C D E
print()


############# is there a path between two nodes #############
def has_path(graph, src, dst):
    visited = [src]
    queue = deque([src])
    while queue:
        node = queue.popleft()
        if node == dst:
            return True
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return False

print("Path A -> D:", has_path(graph, 'A', 'D'))   # True


############# shortest path (number of edges) using BFS #############
def shortest_path(graph, src, dst):
    visited = [src]
    queue = deque([(src, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == dst:
            return dist
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append((i, dist + 1))
    return -1

print("Shortest A -> D:", shortest_path(graph, 'A', 'D'))   # 2


############# count connected components #############
def count_components(graph):
    visited = []
    count = 0
    for node in graph:
        if node not in visited:
            count += 1
            stack = [node]
            while stack:
                cur = stack.pop()
                if cur not in visited:
                    visited.append(cur)
                    stack.extend(graph[cur])
    return count

other = {'1': ['2'], '2': ['1'], '3': []}
print("Components:", count_components(other))   # 2
