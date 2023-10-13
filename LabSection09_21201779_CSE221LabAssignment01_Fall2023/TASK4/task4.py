inp_file = open('input4.txt', 'r')
opt_file = open('output4.txt', 'w')

x = int(inp_file.readline())

info = []
name = []
time = []
place = []

for i in range(x):
    temp = inp_file.readline().strip()
    info.append(temp)
    name.append(temp.split()[0])
    time.append(temp.split()[-1])
    place.append(temp.split()[-3])

for i in range(len(name)):
    for j in range(len(name)-i-1):
        if name[j] > name[j+1]:
            name[j], name[j+1] = name[j+1], name[j]
            info[j], info[j+1] = info[j+1], info[j]

        if name[j] == name[j+1]:
            if time[j] > time[j+1]:
                time[j], time[j+1] = time[j+1], time[j]
                info[j], info[j+1] = info[j+1], info[j]

                if place[j] > place[j+1]:
                    place[j], place[j+1] = place[j+1], place[j]
                    info[j], info[j+1] = info[j+1], info[j]

for i in range(x):
    opt_file.write(f'{info[i]}\n')