"""
Elad Agam
04 - Read lines untill getting an empty lines
Print all the input line by line - backwards
"""

lines = []
while True:
	print "Enter a line"
	line = raw_input()
	if not line == "":
		lines.append(line)
	else:
		break


numoflines =(len(lines)) 
for i in range(numoflines):
	print lines[numoflines-i-1]



