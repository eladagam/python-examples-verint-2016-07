"""
Elad Agam - Classes 
01 - Build Class summer
"""

class Summer(object):

    def __init__(self):
        self.sum = 0
    
    def add(self, number1,number2=0):
        self.sum = self.sum + number1 + number2

    def total(self):
        return str(self.sum)



s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()