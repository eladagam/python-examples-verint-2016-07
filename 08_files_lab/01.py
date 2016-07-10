"""
Elad Agam - Files
01 - Get two files and add the content of the first to the second
"""

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source')
parser.add_argument('-d', '--destination')
args = vars(parser.parse_args())

workingDir =  os.getcwd()

source = os.path.join(workingDir, args['source'])
destination = os.path.join(workingDir, args['destination'])


with open(destination,"a") as fout:
    with open(source,"r") as fin:
        for line in fin:
            fout.write(line)


