"""
Elad Agam
01 - Get 10 numbers and return Max
"""


print "Enter 10 Numbers"
for num in range(10):
    input = int(raw_input())
    if num == 0:
	    maximum=input
    else:    
	    if input > maximum:
		    maximum=input

print "Max = {m}".format(m=maximum)

