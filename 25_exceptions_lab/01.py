"""
Elad Agam - Exceptions 
01 - Do sqrt for inputs in loop - Assert on negative or none-number input 
"""
import math

while True:
    numStr = raw_input('Enter a number:')
    
    try:
        num = float(numStr)
    except ValueError:
        print ("%s is not a number\n" % numStr)
        exit(0)
    
    
    if num < 0:
        raise ValueError("Expected parameter >= 0, Got: %d" % num)

    print math.sqrt(num)
