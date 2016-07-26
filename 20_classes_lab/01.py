"""
Elad Agam - Classes 
01 - Build Class summer
"""

class Summer(object):

    def __init__(self):
        self.sum = 0
    
    def add(self, *numbers):
        self.sum = self.sum + sum(numbers)

    def total(self):
        return str(self.sum)



s = Summer()
t = Summer()

s.add(10, 20,40)
t.add(50)
s.add(30)

# should print 60
print s.total()

# should print 50
print t.total()