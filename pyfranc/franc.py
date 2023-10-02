# -*- coding: utf-8 -*
#!/usr/bin/env python3

from .trigram_utils import asTuples
from .expressions import expressions
from .data import data

from operator import itemgetter
import re

# The maximum distance to add when a given trigram does
# not exist in a trigram dictionary. 
MAX_DIFFERENCE = 300

script = ''
numericData = {}

for script in data:
    languages = data[script] 
    name = ''
    numericData[script] = {}

    for name in languages:
        model = languages[name].split('|')
        trigrams = {}
        weight = len(model)
        while weight > 0:   
            weight -= 1        
            trigrams[model[weight]] = weight

        numericData[script][name] = trigrams     

def lang_detect(value, **kwargs):
    # Minimum sample length.
    MIN_LENGTH = 10
    # Maximum sample length.
    MAX_LENGTH = 2048
    # Set whitelist and blacklist as default.
    only, ignore = [], []
    
    if kwargs.get('minlength'): MIN_LENGTH = kwargs.get('minlength') 
    
    if kwargs.get('whitelist'): only = kwargs.get('whitelist') 
        
    if kwargs.get('blacklist'): ignore = kwargs.get('blacklist') 

    if not value or len(value) < MIN_LENGTH:
        return und()
  
    value = value[slice(0, MAX_LENGTH)]
    script = getTopScript(value, expressions)

    if not script[0] or not (script[0] in numericData):
        if not script[0] or script[1] == 0 or not allow(script[0], only, ignore):
            return und()

        return singleLanguageTuples(script[0])

    return normalize(value, getDistances(asTuples(value), numericData[script[0]], only, ignore))

def normalize(value, distances):
    min = distances[0][1]
    max = len(value) * MAX_DIFFERENCE - min
    index = 0
    
    while index < len(distances): 
        try: 
            distances[index][1] = 1 - (distances[index][1] - min) / max or 0 
        except ZeroDivisionError: 
            distances[index][1] = 0
        index += 1
        
    return distances

def getTopScript(value, scripts):
    topCount = -1
    topScript = ''
    script = ''
    
    for script in scripts:
            count = getOccurrence(value, scripts[script])
            if count > topCount:
                topCount = count
                topScript = script
    
    return topScript, topCount

def getOccurrence(value, expression):
    count = re.findall(expression, value)

    return (len(count) if count else 0) / len(value) or 0

def getDistances(trigrams, languages, only, ignore): 
    languages = filterLanguages(languages, only, ignore) 
    distances = []
    language = ''

    if languages:
        for language in languages:
            distances.append([language, getDistance(trigrams, languages[language])])
      
    return und() if len(distances) == 0 else sorted(distances, key=itemgetter(1), reverse=False)

def getDistance(trigrams, model):
    distance = 0
    index = 0
    
    while index < len(trigrams):
        trigram = trigrams[index]
        difference = MAX_DIFFERENCE
        if trigram[0] in model:
            difference = trigram[1] - model[trigram[0]] - 1
            if difference < 0:
                difference = -difference
        index += 1        
                   
        distance += difference    

    return distance

def filterLanguages(languages, only, ignore):
    if len(only) == 0 and len(ignore) == 0:
        return languages

    filteredLanguages = {}
    language = ''

    for language in languages:
        if allow(language, only, ignore):
            filteredLanguages[language] = languages[language]

    return filteredLanguages

def allow(language, only, ignore):
    if len(only) == 0 and len(ignore) == 0:
        return True
    
    return (len(only) == 0 or language in only) and not language in ignore

def und():
    return singleLanguageTuples('und')

def singleLanguageTuples(language):
    return [[language, 1]]
 