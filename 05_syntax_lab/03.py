"""
Elad Agam
03 - Rand a number (1-10000) and return the sum of its digits
"""

from random import randint

#init sum
sum = 0 

rand = randint(1, 10000)
print "Rand = {R}".format(R=rand)
for num in str(rand):
	sum = sum + int(num)

print "Sum = {Summary}".format(Summary=sum)



