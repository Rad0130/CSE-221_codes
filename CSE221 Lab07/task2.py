file1=open('input2.txt','r')
file2=open('output2.txt','w')

Cities,roads=map(int, file1.readline().split())
edges=[]

for _ in range(roads):
    u,v,w=map(int, file1.readline().split())
    edges.append((u, v, w))

parent = [i for i in range(Cities + 1)]
rank = [0] * (Cities + 1)
size = [1] * (Cities + 1)

def find(A):
    if parent[A] != A:
        parent[A] = find(parent[A])
    return parent[A]

def friendship(A, B):
    root_A = find(A)
    root_B = find(B)

    if root_A != root_B:
        if rank[root_A] < rank[root_B]:
            parent[root_A] = root_B
            size[root_B] += size[root_A]
        elif rank[root_A] > rank[root_B]:
            parent[root_B] = root_A
            size[root_A] += size[root_B]
        else:
            parent[root_B] = root_A
            rank[root_A] += 1

def kruskal(edges):
    edges.sort(key=lambda x: x[2])
    
    mst_edges=[]

    for edge in edges:
        u,v,w=edge

        if find(u)!=find(v):
            mst_edges.append(edge)
            friendship(u, v)
    return mst_edges

min_cost=kruskal(edges)

minimum_cost=0

for edge in min_cost:
    minimum_cost+=edge[2]

file2.write(str(minimum_cost))


file1.close()
file2.close()