file1=open('input1.txt','r')
file2=open('output1.txt','w')

l,s=map(int,file1.readline().split(' '))

arr=list(map(int,file1.readline().split()))

flag=0
for i in range(l):

  for j in range(1,l):
    if arr[i]+arr[j]==s:
      v1=i+1
      v2=j+1
      flag=1
  if flag==1:
    break

if flag==1:
  file2.write(f'{v1} {v2}')
else:
  file2.write('IMPOSIBLE')


file1.close()
file2.close()