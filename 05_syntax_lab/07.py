"""
Elad Agam
07 - Rand numbers (1-100) and let the user guess it 
"""

from random import randint

num1 = randint(1, 100)

while True:
    print "Try to guess my number:"
    num2 = int(raw_input())
    if num1 > num2 or num2 % 7 == 0:
        print "Mine is Greater"
    elif num1 < num2:
	    print "Mine is Smaller"
    else:
	    print "Bingo"
	    break

    




