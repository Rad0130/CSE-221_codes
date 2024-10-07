file1=open('input2.txt','r')
file2=open('output2.txt','w')

N=int(file1.readline())
arr=list(map(int,file1.readline().split()))
l=0
r=N-1

def maximum(arr,l,r):
    if l==r:
        return arr[l]
    
    mid=(l+r)//2
    
    max_l=maximum(arr,l,mid)
    max_r=maximum(arr,mid+1,r)
    
    return max_l if max_l > max_r else max_r

file2.write(str(maximum(arr,l,r)))


file1.close()
file2.close()