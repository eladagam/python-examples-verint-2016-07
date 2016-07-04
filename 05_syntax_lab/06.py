"""
Elad Agam
06 - Rand two numbers (1-10) and find the LCM for both
"""

from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)

print "Randomized {n1} , {n2}".format(n1=num1,n2=num2)

if num1 > num2:
    greater = num1
else:
    greater = num2
 
while True:
    if greater % num1 == 0  and  greater % num2 == 0:
	    lcm = greater
	    break
    greater = greater + 1

print "LCM is {n1}".format(n1=lcm)




