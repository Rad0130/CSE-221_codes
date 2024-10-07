file1=open('input2b.txt','r')
file2=open('output2b.txt','w')

n1=int(file1.readline())
arr1=list(map(int,file1.readline().split(' ')))
n2=int(file1.readline())
arr2=list(map(int,file1.readline().split(' ')))

l1=0
r1=n1-1
l2=0
r2=n2-1

arr=[]

while True:
    if arr1[l1]<arr2[l2]:
        arr.append(arr1[l1])
        l1+=1
    
    elif arr1[l1]>arr2[l2]:
        arr.append(arr2[l2])
        l2+=1

    else:
        arr.append(arr1[l1])
        l1+=1

    if l1>r1:
        arr+=arr2[l2:]
        break
    if l2>r2:
        arr+=arr1[l1:]
        break


file2.write(' '.join(map(str,arr)))

file1.close()
file2.close()