import heapq

file1 = open('input2.txt', 'r')
file2 = open('output2.txt', 'w')

vertex, edges = map(int, file1.readline().split())
graph = {i: {} for i in range(1, vertex + 1)}

for _ in range(edges):
    u, v, w = map(int, file1.readline().split())
    graph[u][v] = w

S, T = map(int, file1.readline().split())

def Dijkstra(graph, Source):
    distance = {i: float('inf') for i in graph}
    parent = {i: None for i in graph}
    distance[Source] = 0
    Q = [(0, Source)]

    while Q:
        c_dist, c_vertex = heapq.heappop(Q)

        if c_dist > distance[c_vertex]:
            continue
        for neighbour, weight in graph[c_vertex].items():
            s_dist = distance[c_vertex] + weight
            if s_dist < distance[neighbour]:
                distance[neighbour] = s_dist
                parent[neighbour] = c_vertex
                heapq.heappush(Q, (s_dist, neighbour))

    return distance

distances = Dijkstra(graph, S)
distances1 = Dijkstra(graph, T)

min_time = float('inf')
meet_Node = None

for Node in graph:
        if Node != S and Node != T:
            time = max(distances[Node],distances1[Node])
            if time < min_time:
                min_time = time
                meet_Node = Node


if min_time == float('inf'):
    file2.write("Impossible")
else:
    file2.write(f"Time {min_time}\nNode {meet_Node}")

file1.close()
file2.close()