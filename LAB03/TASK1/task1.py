ipt_file = open("input1.txt", 'r')
opt_file = open("output1.txt", 'w')

n = int(ipt_file.readline().strip())
data = list(map(int, (ipt_file.readline().strip().split())))


def merge(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # append the remaining elements of a or b to result
    if i < len(a):
        result.extend(a[i:])
    if j < len(b):
        result.extend(b[j:])
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)

opt_file.write(' '.join(map(str, mergeSort(data))))


ipt_file.close()
opt_file.close()
