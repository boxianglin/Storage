name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

table = dict()
# (k,v) = (hour,count)  print: (k,v) in sorted;
for line in handle:
    if line.startswith('From '):
       pos = line.find(':')
       hour = line[pos-2:pos]
       table[hour] = table.get(hour,0)+1

newlst = sorted([(k,v) for k,v,in table.items()])

for k,v in newlst:
	print(k,v)
