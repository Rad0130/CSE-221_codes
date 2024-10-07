file1=open('input5.txt','r')
file2=open('output5.txt','w')

n=int(file1.readline())
arr=list(map(int,file1.readline().split()))
p=0
r=n-1
def QUICKSORT(arr,p,r):
    if p<r:
        q=PARTITION(arr,p,r)
        QUICKSORT(arr,p,q-1)
        QUICKSORT(arr,q+1,r)

def PARTITION(arr,p,r):
    x=arr[r]
    i=p-1
    for j in range(p,r):
        if arr[j]<=x:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

QUICKSORT(arr,p,r)

file2.write(' '.join(map(str,arr)))

file1.close()
file2.close()