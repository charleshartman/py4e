#py4e assignment 7.2

# Use the file name mbox-short.txt as the file name
count = 0
running = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    look = line.find(':')
    fnum = line [look+2:]
    running = float(fnum) + float(running)

print ('Average spam confidence:', running/count)
