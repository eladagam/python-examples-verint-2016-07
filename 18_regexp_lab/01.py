"""
Elad Agam - Regex
01 - print a value of configuration in configuration file 
"""
import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--configuration')
parser.add_argument('-k', '--key')

args = vars(parser.parse_args())

workingDir =  os.getcwd()

#Read inputs and output files - full path 
conf = os.path.join(workingDir, args['configuration'])
key = args['key']


with open(conf,"r") as fin:
    for line in fin:
        res = re.search(key+r'.*=.*(\d)+', line)
        if res is not None:
            print res.group(1)


