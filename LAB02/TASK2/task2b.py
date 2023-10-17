ipt_file = open("input2.txt", 'r')
opt_file = open("output2.txt", 'w')

x = int(ipt_file.readline().strip())
data1 = list(map(int, ipt_file.readline().split()))
z = int(ipt_file.readline().strip())
data2 = list(map(int, ipt_file.readline().split()))

result = []

a = b = 0

while a<x and b<z:
    #Comparing the elements of the two lists
    if data1[a] < data2[b]:
        result.append(data1[a])
        a += 1
    elif data1[a] > data2[b]:
        result.append(data2[b])
        b += 1
    elif data1[a] == data2[b]:
        result.append(data1[a])
        result.append(data2[b])
        a += 1
        b += 1

if a != x:
    result += data1[a:]
if b != z:
    result += data2[b:]

for a in range(len(result)):
    opt_file.write(f"{result[a]} ")

'''
Comments: The while loop will continue as long as there are elements left 
in both data1 and data2. 
After finishing the loop, if there are remaining elements in data1 or data2 
after the while loop, they are appended to the result.
'''