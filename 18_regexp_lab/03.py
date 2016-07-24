"""
Elad Agam - Regex
03 - Replace first and second columns in CSV
"""

import re
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source')
args = vars(parser.parse_args())

workingDir =  os.getcwd()

source = os.path.join(workingDir, args['source'])




with open(source,"r") as fin:
    for line in fin:
        print  re.sub(r'^(\w+),(\w+),', r'\2,\1,', line)        
        #I can't understand why the below did not work!!!
        #print  re.sub(r'^(\w+),(\w+),', lambda m:m.group(1)+","+m.group(0), line)
