"""
Elad Agam - Data structures
01 - Get a list of computer names as agrs
     Look for the names in hosts file, and prin relevnt IP for each name
     If not exists - print an error
"""


import os
import sys

#create a Dictionary for hosts
hosts_dictionary = {}

#get computer names list from the user
names=sys.argv[1:]

#open hosts file and read its content to a dictionary
workingDir =  os.getcwd()
hosts = os.path.join(workingDir, "hosts")

with open(hosts,"r") as fin:
    for line in fin:
        words = line.split("=")
        hosts_dictionary[words[0]]=words[1]

for name in names:
    if name in hosts_dictionary:
        print "IP of %s is %s" %(name , hosts_dictionary[name]),
    else:
        print "%s does not exist" %(name)

