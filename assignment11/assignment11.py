#py4e assignment 11

import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_42.txt"

fh = open(fname)
for line in fh:
    line = line.rstrip()
    num = re.findall('([0-9]+)', line)
    if len(num) > 0:
        print(num)
