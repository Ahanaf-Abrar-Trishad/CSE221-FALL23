ipt_file = open("input4.txt", "r")
opt_file = open("output4.txt", "w")
x, y = list(map(int, ipt_file.readline().split()))

new_arr = []

for i in range(int(x)):
    arr = list(map(int,(ipt_file.readline().strip().split())))
    new_arr.append(arr)

# Bubble sort based on the second element of each sublist
for i in range(int(x)- 1):
    for j in range(int(x) - 1 - i):
        if new_arr[j][0] > new_arr[j + 1][0]:
            new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]

# print(new_arr)

new_list = []

# Initialize an array of pointers to keep track of the last selected activity for each person
peps = [-1] * y

for i in range(int(x)):
    for j in range(int(y)):
        if peps[j] == -1 or new_arr[i][0] >= new_arr[peps[j]][1]:
            new_list.append(new_arr[i])
            peps[j] = i
            break

# print(new_list)
opt_file.write(str(len(new_list)) + "\n")