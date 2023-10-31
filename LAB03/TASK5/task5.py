import random

ipt_file = open("input5.txt", 'r')
opt_file = open("output5.txt", 'w')

n = int(ipt_file.readline().strip())
data = list(map(int, (ipt_file.readline().strip().split())))


def quick_sort(data):

    if len(data) == 1:
        return data
    
    pvt = random.randint(0, len(data)-1) if len(data) > 0 else None

    if pvt is not None:
        left = [x for x in data if x < data[pvt]]
        middle = [y for y in data if y == data[pvt]]
        right = [z for z in data if z > data[pvt]]

        sorted_left = quick_sort(left)
        sorted_right = quick_sort(right)

        return sorted_left + middle + sorted_right
    
    else:
        return []

for x in quick_sort(data):
    opt_file.write(str(x) + ' ')

ipt_file.close()
opt_file.close()