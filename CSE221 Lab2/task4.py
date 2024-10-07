file1=open("input4.txt","r")
file2=open("output4.txt","w")
N,M=map(int,file1.readline().strip().split(" "))

arr=[]
for i in range(N):
    arr.append(file1.readline().strip().split(" "))

for i in range (N):
    min=i
    for j in range(i+1,N):
        if int(arr[min][1])>int(arr[j][1]):
            min=j
    arr[i],arr[min]=arr[min],arr[i]

arr2=[0]*N
a=0
for i in range (N):
    dif=25
    min_d=0
    f=False
    for j in range(M):
        if int(arr[i][0])>=int(arr2[j]) and int(arr[i][0])-int(arr2[j])<dif:
            dif=int(arr[i][0])-int(arr2[j])
            mid_d=j
            f=True
    if f:
        arr2[mid_d]=arr[i][1]
        a+=1
        
file2.write(str(a))

file1.close()
file2.close()