import sys

for x in sys.stdin:
    x=x.strip()
    if " " in x:
        fname,lname=x.split(" ")
    else :
        fname=x
        lname=''
    lname=lname.lower()
    print(" ".join([fname,lname]))