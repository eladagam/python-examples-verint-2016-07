"""
Elad Agam - Exceptions 
02 - open file and print number of lines - assert if not exists 
"""
import os
import sys 


if not os.path.isfile(sys.argv[1]):
    raise ValueError("%s does not exist\n" % fin)

with open(sys.argv[1],"r") as fin:
    print sum(1 for _ in fin)

