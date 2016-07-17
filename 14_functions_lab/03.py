"""
Elad Agam - Functions
03 - Sum the second digit for all inputs
"""

def f(*nums):
    sum=0
    for num in nums:
         sum = sum+ int(str(num)[-2])
    print sum


f(1232,765656,2123)