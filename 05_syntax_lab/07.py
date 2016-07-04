"""
Elad Agam
07 - Rand numbers (1-100) and let the user guess it 
"""

from random import randint

random = randint(1, 100)

while True:
    
    input = int(raw_input('Try to guess my number:'))
    if random > input:
        print "Mine is Greater"
    elif random < input:
	    print "Mine is Smaller"
    else:
	    print "Bingo"
	    break

    




