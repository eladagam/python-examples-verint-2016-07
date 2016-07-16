"""
Elad Agam - Functions
01 - Create two functions Mul and sum
"""

def mysum(*numbers):
    sum=0
    for num in numbers:
        if not type(num) is str:
            sum=sum+num
    print sum

mysum(12,123,"mkcdc")

def mymul(*numbers):
    mul=1
    for num in numbers:
        if not type(num) is str:
            mul=mul*num
    print mul

mymul(12,3,2,"sxsd")