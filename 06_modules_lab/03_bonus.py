"""
Elad Agam - Modules
03 go over all files in current folder recursively  print names of files greater that 1M
"""

import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', default='.')
parser.add_argument('-s', '--fileSize', default=1)
args = vars(parser.parse_args())

path = args['path']
size = int(args['fileSize'])

for folder, subs, files in os.walk(path):
    for filename in files:
	    statinfo = os.stat(os.path.join(folder, filename))
	    if statinfo.st_size > 1000000:
		    print "found file: "+os.path.join(folder, filename)+" size="+str(statinfo.st_size)
		    needToDeletput = raw_input('Delete it? (y/n)')
		    


