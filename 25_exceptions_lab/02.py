"""
Elad Agam - Exceptions 
02 - open file and print number of lines - assert if fail to open
"""
import os
import sys 

sum=0

try:

    with open(sys.argv[1],"r") as fin:
        for _ in fin:
            sum=sum+1
except Exception as e:
    print  ("Sorry, file %s not found" % sys.argv[1])
    exit(0)

print sum
