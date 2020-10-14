e1=int(input("introducem numarul primului elevului"))
e2=int(input("introducem numarul la al doilea elevului"))
e3=int(input("introducem numarul la al treilea elevului"))
p1=int(input("introducem punctajul primulra elevului"))
p2=int(input("introducem punctajul la al doilea elevului"))
p3=int(input("introducem punctajul la al treilea elevului"))
if((p1>p2)and(p1>p3)):
    print(e1)
if((p2>p1)and(p2>p3)):
    print(e2)
if((p3>p2)and(p3>p1)):
    print(e3)