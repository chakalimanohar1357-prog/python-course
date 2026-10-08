# graph = {}

# def add_edge(u, v):
#     if u not in graph:
#         graph[u] = []

#     if v not in graph:
#         graph[v] = []

#     graph[u].append(v)
#     graph[v].append(u)

# add_edge('A', 'B')

# print(graph)


################## BFS ##################

graph = {
    'A': ['B', 'C', 'E'],
    'B': ['C', 'D'],
    'C': ['B', 'A'],
    'D': ['B'],
    'E': ['A']
}

visited = []
queue = []

start = 'A'

visited.append(start)
queue.append(start)

while queue:
    node = queue.pop(0)
    print(node, end=" ")

    for i in graph[node]:
        if i not in visited:
            visited.append(i)
            queue.append(i)

