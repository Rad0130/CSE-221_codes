import heapq

file1 = open('input3.txt', 'r')
file2 = open('output3.txt', 'w')

vertex, edges = map(int, file1.readline().split())
graph = {i: [] for i in range(1, vertex + 1)}

for _ in range(edges):
    u, v, w = map(int, file1.readline().split())
    graph[u].append((v, w))

def min_danger_path(graph, start, end):
    min_danger = [float('inf')] * (vertex+ 1)
    min_danger[start] = 0
    pq = [(0, start)]

    while pq:
        danger, node = heapq.heappop(pq)
        if node == end:
            return danger
        for neighbor, edge_danger in graph[node]:
            new_danger = max(danger, edge_danger)
            if new_danger < min_danger[neighbor]:
                min_danger[neighbor] = new_danger
                heapq.heappush(pq, (new_danger, neighbor))
    return "Impossible"

start, end = 1, vertex
res = min_danger_path(graph, start, end)
file2.write(str(res))

file1.close()
file2.close()