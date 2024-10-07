import heapq

file1=open('input2.txt','r')
file2=open('output2.txt','w')

vertex,edges=map(int, file1.readline().split())
graph={i:[] for i in range(1,vertex+1)}

indegree_dict={}

for _ in range(edges):
    ui,vi=map(int, file1.readline().split())
    graph[ui].append(vi)

for i in range(1,vertex+1):
    count=0
    for Key,value in graph.items():
        if i in value:
            count+=1

    indegree_dict[i]=count


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

def bfs_topo_sort(graph, indegree_dict):
    visited=[0]*(vertex+1)
    
    priority_Q=[]

    result=[]

    for k,v in indegree_dict.items():
        if indegree_dict[k]==0:
            heapq.heappush(priority_Q, k)
            visited[k]=1

            
    while priority_Q:
        c=heapq.heappop(priority_Q)
        result.append(c)
        for neighbour in graph[c]:
            indegree_dict[neighbour]-=1
            if indegree_dict[neighbour]==0:
                heapq.heappush(priority_Q, neighbour)
                visited[neighbour]=1

    file2.write(' '.join(map(str, result)))

if has_cycle(graph, vertex):
    file2.write("IMPOSSIBLE")
else:
    bfs_topo_sort(graph, indegree_dict)    




file1.close()
file2.close()