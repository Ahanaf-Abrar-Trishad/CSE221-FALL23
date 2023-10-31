ipt_file = open("input6.txt", 'r')
opt_file = open("output6.txt", 'w')

n = int(ipt_file.readline().strip())
data = list(map(int, (ipt_file.readline().strip().split())))

def quick_sort(data, left, right, k):
    if left == right:
        return data[left]
    
    pivot = partition(data, left, right)

    if k == pivot:
        return data[pivot]
    elif k < pivot:
        return quick_sort(data, left, pivot - 1, k)
    else:
        return quick_sort(data, pivot + 1, right, k)
    
def partition(data, left, right):
    pivot = data[right]
    j = left - 1
    for i in range(left , right):
        if data[i] <= pivot:
            j += 1
            data[i], data[j] = data[j], data[i]
    data[j+1], data[right] = data[right], data[j+1]
    return j+1

q = int(ipt_file.readline().strip())

for i in range(q):
    k = int(ipt_file.readline().strip())
    kth_smallest = quick_sort(data, 0, n - 1, k - 1)
    opt_file.write(str(kth_smallest) + '\n')

ipt_file.close()
opt_file.close()
