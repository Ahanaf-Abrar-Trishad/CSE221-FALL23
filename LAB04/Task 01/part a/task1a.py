ipt_file = open('input1a_2.txt', 'r')
opt_file = open('output1a_2.txt', 'w')

n, m = map(int, (ipt_file.readline().split()))
adj_matrix = [[0] * (n+1) for i in range(n+1)]
for a in range(m):
    x, y, z = map(int, (ipt_file.readline().split()))
    adj_matrix[x][y] = z
for row in adj_matrix:
    # print(*row)
    print(*row, file=opt_file)