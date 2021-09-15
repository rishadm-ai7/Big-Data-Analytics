#!/usr/bin/python3

import sys

currentword = None
currentvalue = 0

for line in sys.stdin:
    line = line.strip()
    word,value = line.split('\t')
    value= int(value)


    if currentword == word :
        currentvalue+=1

    else:
        if currentword!=None:
            print(" %s\t%s"%(currentword,currentvalue))
        currentword=word
        currentvalue=value

print("%s \t %s"%(currentword,currentvalue))