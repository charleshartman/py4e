#py4e assignment 11

import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_42.txt"

y = 0

fh = open(fname)
for line in fh:
    line = line.rstrip()
    num = re.findall('([0-9]+)', line)
    if len(num) > 0:
#        print(num)
        for x in num:
            num = int(x)
            y = y + num

print(y)
