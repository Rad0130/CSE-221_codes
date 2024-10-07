file1=open('input5.txt','r')
file2=open('output5.txt','w')

N, M, D = map(int, file1.readline().split())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    ui, vi = map(int, file1.readline().split())
    graph[ui].append(vi)
    graph[vi].append(ui)

from collections import deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        visited.add(current)

        if current == end:
            return len(path) - 1, path

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return -1, []

min_time, path = shortest_path(graph, 1, D)

if min_time != -1:
    file2.write(f"Time: {min_time}\n")
    file2.write(f"Shortest Path: {' '.join(map(str, path))}")



file1.close()
file2.close()