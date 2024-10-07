file1=open('input1b.txt','r')
file2=open('output1b.txt','w')

l,s=map(int,file1.readline().split(' '))

arr=list(map(int,file1.readline().split()))

i=0
j=l-1
flag=0
while i<j:
    if arr[i]+arr[j]==s:

      v1=i+1
      v2=j+1
      flag=1
      file2.write(f'{v1} {v2}')
      break
    elif arr[i]+arr[j]<s:
      i+=1
    else:
      j-=1

if flag==0:
  file2.write("IMPOSSIBLE")



file1.close()
file2.close()