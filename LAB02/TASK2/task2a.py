ipt_file = open("input2.txt", 'r')
opt_file = open("output2.txt", 'w')

x = int(ipt_file.readline().strip())
data1 = list(map(int, ipt_file.readline().split()))
z = int(ipt_file.readline().strip())
data2 = list(map(int, ipt_file.readline().split()))

def mergeSort(arr):
	if len(arr) > 1:		
		mid = len(arr)//2
		left = arr[:mid]		
		right = arr[mid:]
		
		mergeSort(left)		
		mergeSort(right)

		a = b = c = 0

		while a < len(left) and b < len(right):
			if left[a] <= right[b]:
				arr[c] = left[a]
				a += 1
			else:
				arr[c] = right[b]
				b += 1
			c += 1

		while a < len(left):
			arr[c] = left[a]
			a += 1
			c += 1

		while b < len(right):
			arr[c] = right[b]
			b += 1
			c += 1
	return arr

result = mergeSort(data1 + data2)

for i in range(len(result)):
    opt_file.write(f"{result[i]} ")


