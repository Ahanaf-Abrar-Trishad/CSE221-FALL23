import math

ipt_file = open("input4.txt", 'r')
opt_file = open("output4.txt", 'w')

n = int(ipt_file.readline().strip())
data = list(map(int, (ipt_file.readline().strip().split())))


def divide_n_conqure(data, max_value = -math.inf):

    if len(data) == 1:
        return data, -math.inf
    
    if len(data) == 2:
        temp = data[0] + pow(data[1], 2)
        if temp >= max_value:
            max_value = temp
        return data, max_value

    mid_ind = len(data)//2
    left = data[:mid_ind]
    right = data[mid_ind:]

    left_part, left_max = divide_n_conqure(left, max_value)
    right_part, right_max = divide_n_conqure(right, max_value)
    merged_array = []

    if left_max >= right_max:
        max_value = left_max
    else:
        max_value = right_max

    big_max = max(left_part)
    i = 0
    while i < len(right_part):
        if max_value <= big_max + pow(right_part[i] , 2):
            max_value = big_max + pow(right_part[i] , 2)
        i += 1

    merged_array.extend(left_part)
    merged_array.extend(right_part)

    return merged_array, max_value

opt_file.write(str(divide_n_conqure(data)[1]))

ipt_file.close()
opt_file.close()