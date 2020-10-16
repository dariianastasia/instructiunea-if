n1 = int(input("dati un numar al elevului "))
n2 = int(input("dati un numar al elevului "))
n3 = int(input("dati un numar al elevului "))
p1 = int(input("dati punctajul primului elev "))
p2 = int(input("dati punctajul elevului 2 "))
p3 = int(input("dati punctajul elevului 3 "))
if ((p1>p2) and (p1>p3)):
    print(n1)
elif ((p2>p1) and (p2>p3)):
    print(n2)
elif ((p3>p1) and (p3>p2)):
    print(n3)
elif ((p1 == p2) and (p1>p3)):
    print(n1,"",n2)
elif ((p1 == p3) and (p1>p2)):
    print(n1,"",n3)
elif ((p3 == p2) and (p3>p1)):
    print(n3,"",n2)
elif (p1 == p2 == p3):
    print(n1,n2,n3)