# -*- coding: utf-8 -*
#!/usr/bin/env python3

from .n_gram import nGram

from operator import itemgetter
import re

def clean(value):
    if value is None:
        return ''

    # trim other symbols
    value = re.sub(r'[\u0021-\u0040]+', ' ', str(value))
    # equal trim in javascript
    value = re.sub(r'^\s+|\s+$', '', value)
    # to lowercase
    value = value.lower()
    #function collapseWhiteSpace(value): 
    value = re.sub(r'\s+', ' ', value)
    return value

def trigrams(value):
    return nGram(' ' + clean(value) + ' ', 3)

def asDictionary(value):
    values = trigrams(value)
    dictionary = {}
    index = 0

    while index < len(values):        
        if values[index] in dictionary:
            dictionary[values[index]] = dictionary[values[index]] + 1 #dictionary.get(values[index], 0) + 1
        else:
            dictionary[values[index]] = 1
        index += 1
          
    return dictionary

def asTuples(value):
    dictionary = asDictionary(value)
    tuples = []
    trigram = ''

    for trigram in dictionary:
        if trigram in dictionary:
            tuples.append([trigram, dictionary[trigram]])

    tuples = sorted(tuples, key=itemgetter(1), reverse=True)
    return tuples

def tuplesAsDictionary(tuples):
    dictionary = {}
    index = -1

    while index < len(tuples):
        dictionary[tuples[index][0]] = tuples[index][1]
        index += 1
        
    return dictionary
