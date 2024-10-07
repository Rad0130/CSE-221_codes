file1=open('input1A.txt','r')
file2=open('output1A.txt','w')

N, M = map(int, file1.readline().split())
edges = []
for _ in range(M):
    ui, vi, wi = map(int, file1.readline().split())
    edges.append((ui, vi, wi))


def create_adjacency_matrix(N, M, edges):

    adjacency_matrix = [[0] * (N+1) for _ in range((N+1))]

    for edge in edges:
        ui, vi, wi = edge
        adjacency_matrix[ui][vi] = wi 

    for row in adjacency_matrix:
        file2.write(f"{' '.join(map(str, row))}\n")

create_adjacency_matrix(N, M, edges)


file1.close()
file2.close()