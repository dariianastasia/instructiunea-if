a=int(input("Introdu nr.1"))
b=int(input("Introdu nr.2"))
c=int(input("Introdu nr.3"))
if ((a>0)and(b>0)and(c>0)and(b>c)):
    print(b)
if((a>0)and(b>0)and(c>0)and(c>b)):
    print(c)
if((a<0)or(b<0)or(c<0)):
    print(b+c)