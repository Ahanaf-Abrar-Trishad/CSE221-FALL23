ipt_file = open("input2_4.txt", 'r')
opt_file = open("output2_4.txt", 'w')

v, e = list(map(int, ipt_file.readline().strip().split()))
visited = [0 for a in range(v+1)]

adj_list = [[]for a in range(v+1)]

for a in range(e):
    f, t = list(map(int, ipt_file.readline().strip().split()))
    adj_list[f].append(t)
    adj_list[t].append(f)

def BFS_Traversal(adj_list, source):
    queue = []
    queue.append(source)
    visited[source] = 1

    while queue:
        temp = queue.pop(0)
        print(temp, end=" ", file=opt_file)

        for x in adj_list[temp]:
            if visited[x] == 0:
                visited[x] = 1
                queue.append(x)

source = 1
BFS_Traversal(adj_list, source)


ipt_file.close()
opt_file.close()