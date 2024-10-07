file1=open('input1A.txt','r')
file2=open('output1A.txt','w')

vertex,edges=map(int, file1.readline().split())
graph={i:[] for i in range(1,vertex+1)}

for _ in range(edges):
    ui,vi=map(int, file1.readline().split())
    graph[ui].append(vi)

def cycle(graph, ver, state, stack):
    state[ver]=1
    stack[ver]=1

    for neighbour in graph[ver]:
        if not state[neighbour]:
            if cycle(graph, neighbour, state, stack):
                return True
        elif stack[neighbour]:
            return True

    stack[ver]=0
    return False

def has_cycle(graph,vertex):
    state = [0]*(vertex+1)
    stack = [0]*(vertex+1)

    for i in range(1, vertex+1):
        if not state[i]:
            if cycle(graph, i, state, stack):
                return True
    
    return False


def dfs(s, visited, stack):
    visited[s]=True

    for i in graph[s]:
        if not visited[i]:
            dfs(i, visited, stack)

    stack.append(s)


def topo_sort():
    visited=[False]*(vertex+1)
    stack=[]

    for i in range(1,vertex+1):
        if not visited[i]:
            dfs(i, visited, stack)

    file2.write(' '.join(map(str, reversed(stack))))

if has_cycle(graph, vertex):
    file2.write('IMPOSSIBLE')
else:
    topo_sort()
    


file1.close()
file2.close()