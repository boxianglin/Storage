handle = open("mbox-short.txt")
table = dict()
for line in handle:
    if line.startswith('From '):
        lst = line.split()
        email = lst[1]
        table[email] = table.get(email, 0) + 1

maxEmail = None
maxCount = 0
for emails, count in table.items():
    if (count > maxCount):
        maxCount = count
        maxEmail = email

print(maxEmail, maxCount)