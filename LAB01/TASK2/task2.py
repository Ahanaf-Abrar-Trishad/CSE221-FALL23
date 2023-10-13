inp_file = open('input2.txt', 'r')
opt_file = open('output2.txt', 'w')

x = inp_file.readline().strip()
x = int(x)

n = list(map(int, inp_file.readline().split()))

def bubbleSort(arr):
  for i in range(len(arr)-1):
    flag = False
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        flag = True
    if flag == False:
      break

  print(arr, file=opt_file)

bubbleSort(n)

# Comment :
"""
To achieve a best-case time complexity of θ(n) for the Bubble Sort algorithm,
the array should already be sorted. In the best-case scenario,
the array is in ascending order, and no swaps are required during the sorting process.
"""