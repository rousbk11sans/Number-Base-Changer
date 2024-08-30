def Integer(x,n):
    a=x//1
    l=[]
    while a!=0:
        b=a//n
        c=a%n
        if c>9:
            c=chr(55+int(c))
            l.append(c)
        else:
            l.append(int(c))
        a=b
    return(l[::-1])

def Fraction(x,n):
    a=x%1
    l=[]
    d=0
    while a!=0 and d<10:
        b=(a*n)//1
        c=(a*n)%1
        if b>9:
            b=chr(55+int(b))
            l.append(b)
        else:
            l.append(int(b))
        a=c
        d+=1
    return(l)

def BaseToggled(x,n):
    a= Integer(x,n)
    b= Fraction(x,n)
    l= a + ["."] +b
    z=""
    for i in l:
        z+=str(i)
    
    print(z)

x = float(input("enter a decimal: "))
n = int(input("enter a base(<11): "))

BaseToggled(x,n)


