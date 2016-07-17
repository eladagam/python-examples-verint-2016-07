"""
Elad Agam - Functions
04 - Gets len + list of words, return a list of all words larger than len
"""

def longer_than(length,*words):
    return [word for word in words if (len(word)>length)]
    

print longer_than(3, 'hit', 'me', 'baby', 'one', 'more', 'time')
