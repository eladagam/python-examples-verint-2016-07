"""
Elad Agam - Classes 
03 - Build Class Widget
"""

class Widget(object):
    listOfBuilt=[]
    def __init__(self,name):
        self.wigName = name
        self.dependList=[]
        

    #get list of Widget objects and add to list
    def add_dependency(self, *dependencies):
        self.dependList=dependencies

    #Go over all object in dependencies list and call build
    def build(self):
        for d in self.dependList:
            if d not in Widget.listOfBuilt:
                
                d.build()
                print d.wigName
                Widget.listOfBuilt.append(d)

luke    = Widget("Luke")
hansolo = Widget("Han Solo")
leia    = Widget("Leia")
yoda    = Widget("Yoda")
padme   = Widget("Padme Amidala")
anakin  = Widget("Anakin Skywalker")
obi     = Widget("Obi-Wan")
darth   = Widget("Darth Vader")
_all    = Widget("All")


luke.add_dependency(hansolo, leia, yoda)
leia.add_dependency(padme, anakin)
obi.add_dependency(yoda)
darth.add_dependency(anakin)

_all.add_dependency(luke, hansolo, leia, yoda, padme, anakin, obi, darth)
_all.build()
# code should print: Han Solo, Padme Amidala, Anakin Skywalker, Leia, Yoda, Luke, Obi-Wan, Darth Vader
# (can print with newlines in between modules)