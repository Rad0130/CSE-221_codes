file1 = open('input6.txt', 'r')
file2 = open('output6.txt', 'w')

R, H = map(int, file1.readline().split())
grid = [file1.readline().strip() for _ in range(R)]

visited = [[0] * H for _ in range(R)]

def DFS(grid, visited, row, column):
    if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] == '#' or visited[row][column]:
        return 0

    visited[row][column] = 1
    diamonds = 0

    if grid[row][column] == 'D':
        diamonds = 1

    diamonds += DFS(grid, visited, row + 1, column)
    diamonds += DFS(grid, visited, row - 1, column)
    diamonds += DFS(grid, visited, row, column + 1)
    diamonds += DFS(grid, visited, row, column - 1)

    return diamonds

total_diamonds = 0

for i in range(R):
    for j in range(H):
        if grid[i][j] == '.' and not visited[i][j]:
            total_diamonds = max(total_diamonds, DFS(grid, visited, i, j))

file2.write(str(total_diamonds))

file1.close()
file2.close()