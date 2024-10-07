file1=open("input1b.txt",'r')
file2=open("output1b.txt","w")

l=file1.readline()

for i in range(int(l)):
  r=file1.readline()
  operand=r[10::]

  if '+' in operand:
    f1,f2=operand.split('+')
    file2.write(f'The result of {operand} is {int(f1)+int(f2)}\n')

  elif '-' in operand:
    f1,f2=operand.split('-')
    file2.write(f'The result of {operand} is {int(f1)-int(f2)}\n')

  elif '*' in operand:
    f1,f2=operand.split('*')
    file2.write(f'The result of {operand} is {int(f1)*int(f2)}\n')

  elif '/' in operand:
    f1,f2=operand.split('/')
    file2.write(f'The result of {operand} is {int(f1)/int(f2)}\n')



file1.close()
file2.close()