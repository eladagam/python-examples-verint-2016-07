"""
Elad Agam
06 - Rand two numbers (1-10) and find the LCM for both
"""

from random import randint

num1 = randint(1, 10)
num2 = randint(1, 10)

print "Randomized {n1} , {n2}".format(n1=num1,n2=num2)
n1 = num1
n2 = num2
lcm = 0
if num1 > num2:
    max = num1
    min = num2 
else:
    max = num2
    min = num1

for i in range(1,max+1):
    if (min*i)%max == 0:
	    lcm = min*i
	    break
        
print "LCM is {n1}".format(n1=lcm)




