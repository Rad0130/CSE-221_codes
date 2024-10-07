file1=open('input4.txt','r')
file2=open('output4.txt','w')

N=int(file1.readline())
A=list(map(int,file1.readline().split()))
arr1=[]
for i in A:
    arr1.append(i)
arr=A[1::]
for i in range(N):
    if arr1[i]<0:
        arr1[i]=arr1[i]*-1

left=0
right=len(arr)-1

for i in range(N-1):
    arr[i]=arr[i]**2

def maximum(arr, left, right):
    if left == right:
        return arr[left]
    
    mid = (left + right) // 2
    
    max_left = maximum(arr, left, mid)
    max_right = maximum(arr, mid + 1, right)
    
    return max_left if max_left > max_right else max_right

max1=maximum(arr,left, right)
m_max=maximum(arr1,left, right)

for i in range(len(arr1)-1,0,-1):
    if arr1[i]==m_max:
        A=A[:i:]
        break

for i in range(len(A)):
    A[i]=A[i]+max1

file2.write(str(maximum(A,0, len(A)-1)))

file1.close()
file2.close()