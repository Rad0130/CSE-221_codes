file1=open('input2a.txt','r')
file2=open('output2a.txt','w')

n1=int(file1.readline())
arr1=list(map(int, file1.readline().split(' ')))
n2=int(file1.readline())
arr2=list(map(int, file1.readline().split(' ')))

arr=arr1+arr2
arr.sort()


file2.write(' '.join(map(str,arr)))

file1.close()
file2.close()
