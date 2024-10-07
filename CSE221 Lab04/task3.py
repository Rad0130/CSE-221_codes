file1=open('input3.txt','r')
file2=open('output3.txt','w')

vertex,edge=map(int, file1.readline().split())
G={i: [] for i in range(1,vertex+1)}

for _ in range(edge):
    ui,vi=map(int, file1.readline().split())
    G[ui].append(vi)
    G[vi].append(ui)

def DFS(G, s):

    stack=[]

    state=[0]*(vertex+1)

    stack.append(s)

    path=[]

    while len(stack)!=0:
        c=stack.pop()
        if state[c]==0:
            path.append(c)
            state[c]=1
        
            for neighbour in reversed(G[c]):
                stack.append(neighbour)

    return (' '.join(map(str, path)))

file2.write(DFS(G, s=1))


file1.close()
file2.close()