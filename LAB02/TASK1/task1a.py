ipt_file = open("input1.txt", 'r')
opt_file = open("output1.txt", 'w')

x , s = list(map(int, ipt_file.readline().split()))
data = list(map(int, ipt_file.readline().split()))

flag = False
for i in range(x):
    for j in range(i+1, x):
        if data[i] + data[j] == s:
            opt_file.write(f"{i+1} {j+1}")
            flag = True
    if flag == True:
        break

if flag == False:
    opt_file.write("IMPOSSIBLE")