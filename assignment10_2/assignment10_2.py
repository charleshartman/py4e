#py4e assignment 10.2

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
for line in fh:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    time = words[5]
    hours = time[0:2]
    if hours not in counts:
        counts[hours] = 1
    else:
        counts[hours] += 1
#print (counts)

lst = list()
for key, val in counts.items():
    brkdwn = (key, val)
    lst.append(brkdwn)

lst = sorted(lst)
for key, val in lst:
    print(key, val)
