"""
Elad Agam - Modules
Get command line arg x and y- print the sum of both  
"""

import sys



if (len(sys.argv) != 3):
    print ('Error - need to send two args')
    sys.exit()

try: 
    print "SUM: " + str(int(sys.argv[1])+int(sys.argv[2]))
except ValueError:
    print ('Error - need to send two numbers')
    

