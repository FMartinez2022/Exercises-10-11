import re


x = []
cnt = 0

fname = input('Enter file: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened: ', fname)
    exit()


for line in fhand:
    line = line.rstrip()
    x_temp = re.findall('^New Revision: ([0-9.]+)', line)
    for v in x_temp:
        v = float(v)
        x = x + [v]

sum = sum(x)
count = float(len(x))
if count:
    cnt = sum / count
print(int(cnt))
