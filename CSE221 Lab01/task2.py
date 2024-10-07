file1=open("input2.txt",'r')
file2=open("output2.txt","w")

n=int(file1.readline())
arr=list(map(int,file1.readline().split()))



def bubbleSort(arr):
  for i in range(len(arr)-1):
    flag=0
    for j in range(len(arr)-i-1):
      if arr[j]>arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        flag=1

    if flag==0:
      break

bubbleSort(arr)

file2.write(' '.join(map(str,arr)))


file1.close()
file2.close()