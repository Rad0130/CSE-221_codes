file1=open('input6.txt','r')
file2=open('output6.txt','w')

N,s=file1.readline().split(' // ')
n=int(N)
arr=list(map(int,file1.readline().split()))
A,b=file1.readline().split(' // ')
a=int(A)

for i in range(a):
    K=int(file1.readline())
    p=0
    r=n-1
    def PARTITION(arr,p,r):
        x=arr[r]
        i=p-1
        for j in range(p,r):
            if arr[j]<=x:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]

        arr[i+1],arr[r]=arr[r],arr[i+1]
        return i+1

    def find_smallest(arr,p,r,K):
        if p==r:
            return arr[p]
        q=PARTITION(arr,p,r)
        if K==q+1:
            return arr[q]
        elif K<q+1:
            return find_smallest(arr,p,q-1,K)
        else:
            return find_smallest(arr,q+1,r,K)

    file2.write(f"{str(find_smallest(arr,p,r,K))}\n")


file1.close()
file2.close()