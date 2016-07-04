"""
Elad Agam
04 - Read lines untill getting an empty lines
Print all the input line by line - backwards
"""

Input = []
while True:
	print "Enter a line"
	line = raw_input()
	if not line == "":
		Input.append(line)
	else:
		break


numoflines =(len(Input)) 
for i in range(numoflines):
	print Input.pop()



