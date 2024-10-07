file1= open("input3.txt","r")
file2= open("output3.txt","w")
N = int(file1.readline())
storage = {i: [] for i in range(N + 2)}

def fibo(n):
    if storage[n]:
        return storage[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibo(n - 1) + fibo(n - 2)
        storage[n] = result
        return result
file2.write(str(fibo(N + 1)))

file1.close()
file2.close()