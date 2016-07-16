"""
Elad Agam - Functions
02 - Check input to function and raise exception if not correct
"""

def f(number, name):
        if  type(number) is str: raise Exception("Firts arg should be a number")
        if not type(name) is str: raise Exception("Secont arg should be a string")
        print "correct"


f(1232,765656)