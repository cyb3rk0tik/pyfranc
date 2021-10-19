# -*- coding: utf-8 -*
#!/usr/bin/env python3

import sys

def nGram(value, n):   
    if type(n) != int or n < 1 or n == sys.maxsize:
      return str(n) + ' is not a valid argument for n-gram.'
      
    nGrams = [] 
    source = ''

    if value == '':
      return nGrams

    source = value if value[slice(0)] else str(value)
    index = len(source) - n + 1

    if index < 1:
      return nGrams

    while index > 0:
      index -= 1    
      nGrams.append(source[slice(index, index + n)])
      
    return list(nGrams)
