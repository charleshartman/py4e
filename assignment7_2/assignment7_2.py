#py4e assignment 7.2

# Use the file name mbox-short.txt as the file name
count = 0
running = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    count = count + 1
    look = line.find(':')
    fnum = line [look+2:]
    #print(fnum)
    #print(count)
    running = float(fnum) + float(running)
    #print(running)

print ('Average spam confidence:', running/count)



    #print(line)
#print("Done")
