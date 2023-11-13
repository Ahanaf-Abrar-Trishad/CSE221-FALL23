ipt_file = open('input1b_2.txt', 'r')
opt_file = open('output1b_2.txt', 'w')

n, m = map(int, (ipt_file.readline().split()))
adj_matrix = [[] for i in range(n+1)]
for a in range(m):
    x, y, z = map(int, (ipt_file.readline().split()))
    adj_matrix[x].append((y, z))
for a in range(n+1):
    print(f'{a}: ', end='',file=opt_file)
    for b in adj_matrix[a]:
        print(f'({b[0]},{b[1]}) ', end='', file=opt_file)
    print(file=opt_file)
