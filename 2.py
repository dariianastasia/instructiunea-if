a=int(input("Introdu numarul primei laturei"))
b=int(input("Introdu numarul la a doua latura"))
c=int(input("Introdu numarul la a treia latura"))
if((a+b>c)and(a+c>b)and(c+b>a)):
    print("Da")
else:
    print("Nu")