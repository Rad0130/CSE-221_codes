file1=open("input1a.txt",'r')
file2=open("output1a.txt","w")

l=int(file1.readline())

for i in range(l):
  num=int(file1.readline())
  if num%2==0:
    file2.write(f'{num} is an even number\n')

  else:
    file2.write(f'{num} is an odd number\n')

file1.close()
file2.close()