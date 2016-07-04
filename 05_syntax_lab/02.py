"""
Elad Agam
02 - Rand 7 numbers (1-100) and return the sum of all
In case The sum divides by 7 --> print Boom 
"""

from random import randint

#init sum
sum = 0 

for num in range(7):
	sum = sum + randint(1, 100)

print "Sum = {Summary}".format(Summary=sum)
if sum % 7 == 0:
	print "Boom"


