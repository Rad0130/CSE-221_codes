import math

file1 = open('input4.txt', 'r')
file2 = open('output4.txt', 'w')

N, X = map(int, file1.readline().split())

coin_denominations = list(map(int, file1.readline().split()))
table = [[0] * (X + 1) for _ in range(N + 1)]

for i in range(1, N + 1):  
    coin = coin_denominations[i - 1]
    for j in range(X + 1):
        if j == 0:
            table[i][j] = 0
        elif i == 1:
            if j % coin == 0:
                table[i][j] = j // coin
            else:
                table[i][j] = math.inf
        else:
            if j < coin:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = min(table[i - 1][j], 1 + table[i][j - coin])

file2.write(str(table[-1][-1]))

file1.close()
file2.close()