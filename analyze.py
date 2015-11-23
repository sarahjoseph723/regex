import re
from collections import Counter

#RETURNS list of all names found
# r: list of strings to be analyzed
def who(r):
    exp = "[A-Z][a-zA-Z]*\s[A-Z][a-zA-Z]*"
    result = []
    #thing is one string in the list
    for thing in r:
        #ADD REGULAR EXPRESSION TO GET RID OF WORDS THAT ARE OBVIOUSLY NOT NAMES
        temp = re.findall(exp,thing)
        for item in temp:
            result.append(item)
    return result

#RETURNS list of all dates found
# r: list of strings to be analyzed
def when(r):
    #exp handles 11/21/15 or November 21, 2015
    exp = "[0-9]?[0-9]/[0-9]?[0-9]/[0-9][0-9]|[A-Z][a-z]*\s[0-9]?[0-9],\s[0-9]{4}"
    result = []
    #thing is one string in the list
    for thing in r:
        #ADD SAME REGULAR EXPRESSION AS ABOVE TO GET RID OF WORDS THAT ARE OBVIOUSLY NOT NAMES
        temp = re.findall(exp,thing)
        for item in temp:
            result.append(item)
    return result

#RETURNS most frequent item in a list
def getMode(x):
    dict={}
    for item in x:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    n=dict.keys()
    m=dict.values()
    print x
    return n[m.index(max(m))]
