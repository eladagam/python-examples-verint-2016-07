"""
Elad Agam
05 - Rand numbers in loop (1-1000000) and stop only if it manage to rand a number that divides to 7, 13, and 15
"""

from random import randint

 
while True:
	num = randint(1, 1000000)
	if num % 7 == 0 and num % 13 == 0 and num % 15 == 0:
		print "Found a number that divides to 7 13 15 => {n}".format(n=num)
		break


