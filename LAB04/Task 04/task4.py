ipt_file = open("input4_5.txt", 'r')
opt_file = open("output4_5.txt", 'w')

v, e = list(map(int, ipt_file.readline().strip().split()))
visited = [0 for a in range(v+1)]

adj_list = [[]for a in range(v+1)]

for i in range(e):
    f, t = list(map(int, ipt_file.readline().strip().split()))
    adj_list[f].append(t)


def Cycle_Detect(adj_list, selected):
    visited[selected] = 1
    
    for adj_node in adj_list[selected]:
        if visited[adj_node] == 0:
            Got_Cycle = Cycle_Detect(adj_list, adj_node)
            if(Got_Cycle):
                return True
            
        elif visited[adj_node] == 1:
            return True

    visited[selected] = 2
    return False

Cycle_Exist = False

for i in range(1, v+1):
    if visited[i] == 0:
        is_Cyclic= Cycle_Detect(adj_list, i)
        if is_Cyclic:
            Cycle_Exist = True
            break
    
if Cycle_Exist:
    print("YES", file=opt_file)
else:
    print("NO", file=opt_file)

ipt_file.close()
opt_file.close()