#py4e assignment 7.1

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
for line in inp:
    line = line.rstrip()
capinp = inp.upper()
print(capinp)
