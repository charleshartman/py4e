#py4e assignment 9.4

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
for line in fh:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    #print(words[1])
    if words[1] not in counts:
        counts[words[1]] = 1
    else:
        counts[words[1]] += 1
#print(counts)
bigcount = None
bigword = None
for words,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = words
        bigcount = count

print(bigword, bigcount)
