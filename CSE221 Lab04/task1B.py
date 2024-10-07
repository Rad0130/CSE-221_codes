file1=open('input1B.txt','r')
file2=open('output1B.txt','w')

N,M=map(int, file1.readline().split())

edges=[]
adjacency_dic= {i: [] for i in range(N+1)}

for _ in range(M):
    ui, vi, wi= map(int, file1.readline().split())
    edges.append((ui, vi, wi))

for edge in edges:
    ui, vi, wi= edge
    adjacency_dic[ui].append((vi, wi))

for key,val in adjacency_dic.items():
    file2.write(f"{key} : {' '.join(map(str, val))}\n")

file1.close()
file2.close()