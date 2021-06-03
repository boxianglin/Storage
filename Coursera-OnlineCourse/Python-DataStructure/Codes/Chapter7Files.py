'''

7.1 Write a program that prompts for a file name,
 then opens that file and reads through the file,
 and print the contents of the file in upper case.
 Use the file words.txt to produce the output below.

'''

# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    quit()

for line in fh:
    line = line.rstrip()
    print(line.upper())

'''
7.2 Write a program that prompts for a file name, 
 then opens that file and reads through the file,
  looking for lines of the form:
  
  Count these lines and extract the floating point 
  values from each of the lines and compute the average 
  of those values and produce an output as shown below.
'''


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    quit()
total = 0
data = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(":")
    data = line[pos+1:]
    data = float(data)
    total = total + data
    count = count + 1
average = total / count
print("Average spam confidence:",average)






