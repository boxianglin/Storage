# 8.4
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    sublist = line.split()
    for sub in sublist:
        if sub in lst:continue
        lst.append(sub)
lst.sort()
print(lst)


#8.5

fh = open("mbox-short.txt")
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        list = line.split()
        email = list[1]
        print(email)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
