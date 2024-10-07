file1=open('input3.txt','r')
file2=open('output3.txt','w')

vertex,edges=map(int, file1.readline().split())
graph={i:[] for i in range(1,(vertex+1))}
transposed_graph={i:[] for i in range(1,(vertex+1))}

for _ in range(edges):
    ui,vi=map(int, file1.readline().split())
    graph[ui].append(vi)
    transposed_graph[vi].append(ui)

def dfs(s, visited, stack):
    visited[s]=True

    for i in graph[s]:
        if not visited[i]:
            dfs(i, visited, stack)

    stack.append(s)


def make_stack():
    visited=[False]*(vertex+1)
    stack=[]

    for i in range(1,vertex+1):
        if not visited[i]:
            dfs(i, visited, stack)
    
    return stack

m_stack=make_stack()

def dfs_scc(graph, vertex, visited, scc):
    visited[vertex]=True
    scc.append(vertex)
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs_scc(graph, neighbor, visited, scc)

def koraju_algo(transposed_graph,vertex):
    visited=[False]*(vertex+1)
    sccs = []
    while m_stack:
        vertex = m_stack.pop()
        if not visited[vertex]:
            scc = []
            dfs_scc(transposed_graph, vertex, visited, scc)
            sccs.append(scc)

    return sccs

components=koraju_algo(transposed_graph,vertex)

for i in components:
    file2.write(f"{' '.join(map(str, reversed(i)))}\n")


file1.close()
file2.close()