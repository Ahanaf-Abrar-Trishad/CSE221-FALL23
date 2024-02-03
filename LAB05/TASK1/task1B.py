iptfile = open("input1b_1.txt", "r")
optfile = open("output1b_1.txt", "w")

v, e = list(map(int, iptfile.readline().strip().split()))
adj_list = [[] for i in range(v+1)]
visited = [0 for i in range(v+1)]
visited_cycle = [0 for i in range(v+1)]
indegre = [0 for i in range(v+1)]


def BFS_Topological_Sort(adj_list, indegre):
    queue = []
    for i in range(1, (v+1)):
        if indegre[i] == 0:
            queue.append(i)
    result = []      
    while queue:
        temp = queue.pop(0)
        result.append(temp)
        for adj_node in adj_list[temp]:
            indegre[adj_node] -= 1
            if indegre[adj_node] == 0:
                queue.append(adj_node)
                    
    return result
                
def Cycle_Detect(selected):
    visited_cycle[selected] = 1
    for adj_node in adj_list[selected]:
        if visited_cycle[adj_node] == 0:
            Got_Cycle = Cycle_Detect(adj_node)
            if(Got_Cycle):
                return True
        elif visited_cycle[adj_node] == 1:
            return True

    visited_cycle[selected] = 2
    return False

for i in range(1, (e+1)):
    f, t = list(map(int, iptfile.readline().strip().split()))
    adj_list[f].append(t)
    indegre[t] += 1
    

Cycle_Exist = False
for i in range(1, v+1):
    if visited_cycle[i] == 0:
        is_Cyclic= Cycle_Detect(i)
        if is_Cyclic:
            Cycle_Exist = True
            break
    
if Cycle_Exist:
    print("IMMPOSSIBLE", file=optfile)
else:
    print(*BFS_Topological_Sort(adj_list, indegre), file=optfile)
  

iptfile.close()
optfile.close()