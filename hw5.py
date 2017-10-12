import operator
import re

openedfile = open('actualdata.txt')
sum1 = []

for x in openedfile:
	x = x.strip()
	line1 = re.findall("[0-9]+",x)
	for y in line1:
		sum1.append(int(y))

print(sum(sum1))
