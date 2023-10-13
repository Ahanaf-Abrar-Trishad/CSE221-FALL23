inp_file = open('input1a.txt', 'r')
opt_file = open('output1a.txt', 'w')

x = (inp_file.readline())
x = int(x)

for i in range (x):
  n = inp_file.readline()
  n = int(n)
  if n%2==0:
    opt_file.write(f'{str(n)} is an Even number.\n')
  else:
    opt_file.write(f'{str(n)} is an Odd number.\n')

opt_file.flush()