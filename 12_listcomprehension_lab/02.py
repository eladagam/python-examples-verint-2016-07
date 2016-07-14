"""
Elad Agam - List comprehansion 
02 - Build all combinations of 3 letter words 
"""

letters  = [chr(letter) for letter in range(97,123)]
combinations = [x+y+z for x in letters for y in letters for z in letters]
print combinations