#!/usr/bin/python3

# import sys
# currentyear=None
# count=1
# total=0.0
# for line in sys.stdin:
#     line = line.strip()
#     year,value = line.split("\t")
#     value= float(value)
#
#     if year==currentyear:
#         total+=value
#         count+=1
#
#     else:
#         if currentyear:
#             avg=total/count
#             print("%s\t%.2f"%(currentyear,avg))
#
#         currentyear=year
#         total=value
#         count=1
#
# avg=total/count
# print("%s\t%.2f" % (currentyear, avg))


#Q2

# import sys
# currentmonth=None
# total=0
# for line in sys.stdin:
#     line=line.strip()
#     words=line.split("\t")
#     month=words[0]
#     value=words[1]
#     value=int(value)
#
#     if month==currentmonth:
#         total+=value
#
#     else :
#         if currentmonth:
#             print("%s\t%s"%(currentmonth,total))
#         currentmonth=month
#         total=value
#
# print("%s\t%s"%(currentmonth,total))
#
#


#Q3 Number of months consumed more than 30 unit in each year?

# import sys
# count=1
# currentyear=None
# for line in sys.stdin:
#     line=line.strip()
#     word=line.split("\t")
#     year=word[0]
#     for value in word:
#         if currentyear==year:
#             count+=1
#         else:
#             if currentyear:
#                 print(str(count)+"months consumed more than 30 unit in the year "+str(currentyear))
#             currentyear=year
#             count=1
#
# print(str(count) + "months consumed more than 30 unit in the year " + str(currentyear))


# Q.4top three consuming months in each year?

#DIDNT GET IT

#Q.5 total money paid by institution in months feb to june if charge is 6 rs/unit?

import sys
sum=0
for line in sys.stdin:
    line=line.strip()
    word=line.split("\t")
    month=int(word[0])
    amount=int(word[1])


    if month>=2 and month<=6:
        sum+=amount

print("The company paid Rs. %s"%(sum*6))





