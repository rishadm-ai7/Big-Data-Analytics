#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split(" ")
    name = words[0]
    subject=words[2]
    marks=int(words[3])
    if marks>50:
        print("%s,%s,%s"%(name,subject,marks))
