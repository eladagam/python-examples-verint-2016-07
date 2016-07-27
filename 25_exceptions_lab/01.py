"""
Elad Agam - Exceptions 
01 - Do sqrt for inputs in loop - Assert on negative or none-number input 
"""
import math

while True:
    numStr = raw_input('Enter a number:')
    
    try:
        print math.sqrt(float(numStr))

    except ValueError as e:
        if e.message == 'math domain error':
            print ("%s Number is not possitive\n" %numStr)
        else:
            print ("%s is not a number\n" % numStr)
   
        exit(0)
    
    

    
    

    
