#py4e assignment 8.4

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #line = line.rstrip()
    words = line.split()
    for x in words:
        if x not in lst:
            lst.append(x)

lst.sort()
print(lst)
