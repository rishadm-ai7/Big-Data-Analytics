#!/usr/bin/python3

import sys
currentname=None
currentmark=0

for line in sys.stdin:
    line=line.strip()
    name,mark = line.split("\t")
    mark = int(mark)

    if currentname==name:
        currentmark+=mark

    else:
        if currentname!=None :
            print("%s\t%s"%(currentname,currentmark))
        currentname = name
        currentmark = mark

print("%s\t%s"%(currentname,currentmark))





