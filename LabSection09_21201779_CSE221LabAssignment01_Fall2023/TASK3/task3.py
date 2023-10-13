inp_file = open('input3.txt', 'r')
opt_file = open('output3.txt', 'w')

x = int(inp_file.readline())

iD = list(map(int, inp_file.readline().split()))
mark = list(map(int, inp_file.readline().split()))

for i in range(x):
    # Find the minimum element in remaining unsorted array
    min_idx = i
    for j in range(i, x):
        # Sorting marks of students
        if mark[min_idx] < mark[j]:
            min_idx = j   
        # Sorting IDs of students if marltiple students have same mark
        if mark[min_idx] == mark[j]:
            if iD[min_idx] > iD[j]:
                min_idx = j      
    # Swap the found minimum element with the first element	 
    mark[i], mark[min_idx] = mark[min_idx], mark[i]
    iD[i], iD[min_idx] = iD[min_idx], iD[i]

for i in range(x):
    opt_file.write(f'ID: {iD[i]} Mark: {mark[i]}\n')




    
