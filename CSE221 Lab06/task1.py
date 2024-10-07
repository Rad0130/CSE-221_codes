import heapq

file1=open('input1.txt','r')
file2=open('output1.txt','w')

vertex,edges=map(int, file1.readline().split())
graph={i:{} for i in range(1,vertex+1)}

for _ in range(edges):
    u,v,w=map(int, file1.readline().split())
    graph[u][v]=w

S=int(file1.readline())

def Dijkstra(graph,S):
    distance={i: float('inf') for i in graph}
    parent={i: None for i in graph}
    distance[S]=0
    Q=[(0,S)]

    while Q:
        c_dist,c_vertex=heapq.heappop(Q)

        if c_dist>distance[c_vertex]:
            continue
        for neighbour, weight in graph[c_vertex].items():
            s_dist=distance[c_vertex]+weight
            if s_dist<distance[neighbour]:
                distance[neighbour]=s_dist
                parent[neighbour]=c_vertex
                heapq.heappush(Q,(s_dist,neighbour))

    return distance

distances= Dijkstra(graph, S)

for Node in range(1,vertex+1):
    if distances[Node]==float('inf'):
        distances[Node]=-1
    file2.write(str(distances[Node])+" ")

file1.close()
file2.close()