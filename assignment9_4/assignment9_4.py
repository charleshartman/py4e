#py4e assignment 9.4

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
counts = dict()
for line in fh:
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    print(words[1])
    for word in words[1]:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
