import re

fHandle = open('regex_sum_1268623.txt')

total = 0;
for line in fHandle:
    sumlist = re.findall('[0-9]+',line)
    sumlist = list(map(int,sumlist))
    total = total + sum(sumlist)

print(total)

s = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
news = re.findall('\S+?@\S+',s)
newa = re.findall('\S?@\S+',s)
print(news,newa)