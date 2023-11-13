ipt_file = open("input6_7.txt", "r")
opt_file= open("output6_7.txt", "w")
R, H = ipt_file.readline().strip().split(' ')
grid = []
for i in range(int(R)):
    line = ipt_file.readline().strip('\n')
    grid.append(line)

def DFS(grid, visited, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] == '#':
        return 0
    
    visited[i][j] = True
    diamonds = 0

    if grid[i][j] == 'D':
        diamonds += 1
    diamonds += max(DFS(grid, visited, i+1, j), DFS(grid, visited, i-1, j), DFS(grid, visited, i, j+1), DFS(grid, visited, i, j-1))
    visited[i][j] = False

    return diamonds

visited = [[False]*int(H) for i in range(int(R))]
maxDiamond = 0
for i in range(int(R)):
    for j in range(int(H)):
        if grid[i][j] == '.':
            diamonds = DFS(grid, visited, i, j)
            maxDiamond = max(maxDiamond, diamonds)
opt_file.write(str(maxDiamond))
print(maxDiamond)


ipt_file.close()
opt_file.close()