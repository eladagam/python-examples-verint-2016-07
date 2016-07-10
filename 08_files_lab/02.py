"""
Elad Agam - Files
02 - Get three files and MERGE the content of first two to the third 
"""

import argparse
import os
import itertools
 


parser = argparse.ArgumentParser()
parser.add_argument('-s1', '--source1')
parser.add_argument('-s2', '--source2')
parser.add_argument('-d', '--destination')

args = vars(parser.parse_args())

workingDir =  os.getcwd()

#Read inputs and output files - full path 
source1 = os.path.join(workingDir, args['source1'])
source2 = os.path.join(workingDir, args['source2'])
destination = os.path.join(workingDir, args['destination'])


#Merge two input files to the output file
with open(destination,"w") as fout:
    with open(source1,"r") as fin1:
        with open(source2,"r") as fin2:
            for i in itertools.izip_longest(fin1, fin2):
                if i[0]!=None:
                    fout.write(i[0])
                if i[1]!=None:
                    fout.write(i[1])
            