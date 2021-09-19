#!/usr/bin/python3
import calendar as cal

#Q3 Number of months consumed more than 30 unit in each year?


# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     words = line.split("\t")
#     year = words[0]
#
#     for value in words:
#         if value!=year and int(value)>30:
#             print("%s\t%s"%(year,value))


#Q4top three consuming months in each year?

# import sys
#
# for line in sys.stdin:
#     line=line.strip()
#     word=line.split("\t")
#     year=word[0]
#
#     if word!=year:
#         for i,month in enumerate(word):
#             print("%s,%s"%(i,month))


#Q5 total money paid by institution in months feb to june if charge is 6 rs/unit?

import sys
for line in sys.stdin:
    line=line.strip()
    word=line.split("\t")
    year=word[0]
    for i,cons in enumerate(word):
        if cons!=year:
            print("%s\t%s"%(i,cons))