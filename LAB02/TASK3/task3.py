ipt_file = open("input3.txt", "r")
opt_file = open("output3.txt", "w")
x = ipt_file.readline().strip()

new_arr = []

for i in range(int(x)):
    arr = list(map(int,(ipt_file.readline().strip().split())))
    new_arr.append(arr)

# Bubble sort based on the second element of each sublist
for i in range(int(x)- 1):
    for j in range(int(x) - 1 - i):
        if new_arr[j][1] > new_arr[j + 1][1]:
            # Swap if the second element is greater
            new_arr[j], new_arr[j + 1] = new_arr[j + 1], new_arr[j]

# print(new_arr)

new_list = []

# # Loop through the new_arr
# for i in range(int(x)):
#     if i == 0:
#         new_list.append(new_arr[i])
#     else:
#         if new_arr[i-1][1] <= new_arr[i][0]:
#             new_list.append(new_arr[i])
            
# print(new_list)

peps = [-1] * 1

for i in range(int(x)):
    for j in range(int(1)):
        if peps[j] == -1 or new_arr[i][0] >= new_arr[peps[j]][1]:
            new_list.append(new_arr[i])
            peps[j] = i
            break
        
# print(new_list)

opt_file.write(str(len(new_list)) + "\n")
for i in range(len(new_list)):
    opt_file.write(str(new_list[i][0]) + " " + str(new_list[i][1]) + "\n")


