inp_file = open('input1b.txt', 'r')
opt_file = open('output1b.txt', 'w')

x = inp_file.readline()
x = int(x)

for i in range (x):
  n = inp_file.readline().strip()
  p = n.split(' ')

  if p[2]=="+":
    opt_file.write(f'The result of {p[1]} + {p[3]} is {str(int(p[1]) + int(p[3]))}\n')
  elif p[2]=="-":
      opt_file.write(f'The result of {p[1]} - {p[3]} is {str(int(p[1]) - int(p[3]))}\n')
  elif p[2]=="/":
      opt_file.write(f'The result of {p[1]} / {p[3]} is {str(int(p[1]) / int(p[3]))}\n')
  elif p[2]=="*":
      opt_file.write(f'The result of {p[1]} * {p[3]} is {str(int(p[1]) * int(p[3]))}\n')
