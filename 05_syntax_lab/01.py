"""
Elad Agam
01 - Get 10 numbers and return Max
"""

#init max
print "Enter a Number"
input = raw_input()
Max = input

for num in range(9):
	print "Enter another Number"
	input = raw_input()
	if input > Max:
		Max=input

print "Max = {maximum}".format(maximum=Max)

