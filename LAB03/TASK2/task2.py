ipt_file = open("input2.txt", 'r')
opt_file = open("output2.txt", 'w')

n = int(ipt_file.readline().strip())
data = list(map(int, (ipt_file.readline().strip().split())))

def findMax(arr, low, high):
    if low == high: # when there's only one element in the array
        return arr[low]
    else:
        mid = (low + high)//2
        leftMax = findMax(arr, low, mid) # find the maximum of the left subarray
        rightMax = findMax(arr, mid + 1, high) # find the maximum of the right subarray
        return max(leftMax, rightMax) # return the maximum of the two subarray maxima


result = findMax(data, 0, n - 1)
opt_file.write(str(result))


'''''
The time complexity of the `findMax` function using the 
divide-and-conquer approach to find the maximum value is O(N).
'''''

ipt_file.close()
opt_file.close()