file1=open('input4.txt','r')
file2=open('output4.txt','w')

N, M=map(int, file1.readline().split())
graph={i: [] for i in range(1,N+1)}

for _ in range(M):
    ui,vi=map(int, file1.readline().split())
    graph[ui].append(vi)

def cycle(graph, vertex, state, stack):
    state[vertex]=1
    stack[vertex]=1

    for neighbour in graph[vertex]:
        if not state[neighbour]:
            if cycle(graph, neighbour, state, stack):
                return True
        elif stack[neighbour]:
            return True

    stack[vertex]=0
    return False

def has_cycle(graph,N):
    state = [0]*(N+1)
    stack = [0]*(N+1)

    for vertex in range(1, N+1):
        if not state[vertex]:
            if cycle(graph, vertex, state, stack):
                return True
    
    return False

if has_cycle(graph, N):
    file2.write("YES")
else:
    file2.write("NO")


file1.close()
file2.close()