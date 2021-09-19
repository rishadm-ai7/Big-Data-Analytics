#!/usr/bin/python3

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Q1:Total marks Scored by each student?
#
# import sys
# currentname=None
# currentmark=0
#
# for line in sys.stdin:
#     line=line.strip()
#     name,mark = line.split("\t")
#     mark = int(mark)
#
#     if currentname==name:
#         currentmark+=mark
#
#     else:
#         if currentname!=None :
#             print("%s\t%s"%(currentname,currentmark))
#         currentname = name
#         currentmark = mark
#
# print("%s\t%s"%(currentname,currentmark))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Q2:Average marks Scored by each student?

# import sys
# currentname=None
# currentmark=0
# count=1
#
# for line in sys.stdin:
#     line=line.strip()
#     name,mark = line.split("\t")
#     mark = int(mark)
#
#     if currentname==name:
#         currentmark+=mark
#         count+=1
#
#     else:
#         if currentname!=None :
#             currentmark/=count
#             print("%s\t%s"%(currentname,currentmark))
#         currentname = name
#         currentmark = mark
#         count = 1
#
# currentmark/=count
# print("%s\t%s"%(currentname,currentmark))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Q4:List all students passed in physics?(passmark--above 50)

# import sys
# currentname="physics"
# for line in sys.stdin:
#     line=line.strip()
#     name,mark=line.split(",")
#     mark=int(mark)
#     if mark>50:
#         print("%s,pass"%(name))


# import sys
# countch=0
# countph=0
# countcs=0
# countma=0
# for line in sys.stdin:
#     line=line.strip()
#     subject,mark=line.split(",")
#     mark=int(mark)
#
#     if subject == "chemistry":
#         if mark>50:
#             countch+=1
#
#     elif subject == "cs":
#         if mark > 50:
#             countcs += 1
#
#     elif subject == "physics":
#         if mark>50:
#             countph+=1
#
#     elif subject == "maths":
#         if mark>50:
#             countma+=1
#
#
# print("Students passed in Chemistry =%s, Maths =%s, cs=%s,physics=%s"%(countch,countma,countcs,countph))
# chemistry- rahul(30),akhil(25)
# import sys
# currentsub=None
# currentname=None
# for line in sys.stdin:
#     line=line.strip()
#     subject,name,mark=line.split(",")
#
#     if currentsub==subject:
#         currentname += ','+name+'('+mark+')'
#
#     else:
#         if currentsub:
#             print('%s- %s'%(currentsub,currentname))
#
#         currentsub = subject
#         currentname = name + '(' + mark +')'
# print('%s- %s' % (currentsub, currentname))
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>Qlast

import sys
currentname=None
currentsub=None
currentmark=0
for line in sys.stdin:
    line=line.strip()
    name,subject,mark=line.split(",")

    if currentname==name:
        currentmark+=int(mark)
        currentsub += ','+subject+'('+mark+')'

    else:
        if currentsub:
            print('%s- %s--%s'%(currentname,currentsub,currentmark))

        currentname=name
        currentmark=int(mark)
        currentsub = subject + '(' + mark +')'
print('%s- %s--%s' % (currentname,currentsub,currentmark))
