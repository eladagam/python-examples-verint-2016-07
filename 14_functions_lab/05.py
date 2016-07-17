"""
Elad Agam - Functions
05 - lamda 
"""

def groupby(function,*args):
    ret = {}
    for n in args:
        if ret.has_key(function(n)):
            ret[function(n)].append(n)
        else:
            ret[function(n)] = [n,]
    return ret
    

print groupby(lambda(s): s[0], 'hello', 'hi', 'help', 'bye', 'here')