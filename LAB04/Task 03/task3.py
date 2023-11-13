ipt_file = open("input3_3.txt", 'r')
opt_file = open("output3_3.txt", 'w')

v, e = list(map(int, ipt_file.readline().strip().split()))
visited = [0 for a in range(v+1)]
adj_list = [[]for a in range(v+1)]

for i in range(e):
    f, t = list(map(int, ipt_file.readline().strip().split()))
    adj_list[f].append(t)
    adj_list[t].append(f)


def DFS_Traversal(adj_list, selected):
    visited[selected] = 1
    print(selected, end=" ", file=opt_file)
    for adj_node in adj_list[selected]:
        if visited[adj_node] == 0:
            DFS_Traversal(adj_list, adj_node)

selected = 1
DFS_Traversal(adj_list, selected)


ipt_file.close()
opt_file.close()