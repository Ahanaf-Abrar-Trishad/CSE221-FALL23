ipt_file = open("input1.txt", 'r')
opt_file = open("output1.txt", 'w')

x , s = list(map(int, ipt_file.readline().split()))
data = list(map(int, ipt_file.readline().split()))

dict = {}

for i in range(x):
    rem = (s - data[i])
    if rem in dict:
        opt_file.write(f"{dict[rem]} {i+1}")
        break
    else:
        dict[data[i]] = i+1
else:
    opt_file.write("IMPOSSIBLE")







