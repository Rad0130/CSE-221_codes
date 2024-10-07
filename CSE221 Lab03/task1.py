file1=open('input1.txt','r')
file2=open('output1.txt','w')

N=int(file1.readline())
arr=list(map(str,file1.readline().split()))

def merge(a, b):
  arr=[]
  i,j=0,0
  while i<len(a) and j<len(b):
    if a[i]>=b[j]:
      arr.append(a[i])
      i+=1
    else:
      arr.append(b[j])
      j+=1
  arr+=a[i::]
  arr+=b[j::]
  return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    else:
        mid = len(arr)//2
        a = mergeSort(arr[mid:])
        b = mergeSort(arr[:mid])
  
    return merge(a, b) 

file2.write(' '.join(map(str,mergeSort(arr))))

file1.close()
file2.close()