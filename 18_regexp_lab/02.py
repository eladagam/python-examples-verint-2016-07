"""
Elad Agam - Regex
02 - toCamelCase get string with '_' and replace to CamelCase
"""

import re
import argparse
import os

def toCamelCase(text):
    str =  re.sub(r'_[a-z]', lambda m: m.group(0).upper(), text)
    print re.sub(r'_','' , str)

toCamelCase("no_more_shall_we_part")