from fractions import Fraction
a=7
b=7
p=23

n=7
def add(r1,r2):
    q=0
    t1=0
    t2=1
    t=0
    i=0
    while r1!=1:
        d=divmod(r1,r2)
        q=d[0]
        rem=d[1]
        #print(q,r1,r2,rem,t1,t2,t)
        r1=r2
        r2=rem
        t=t1-(t2*q)
        t1=t2
        t2=t
    return t1

P=(7,12)
Q=(7,12)
print("a=",1)
print("b=",b)
print("p=",p)
print("P=",P)
print("Q=",Q)
Px=P[0]
Py=P[1]
Qx=Q[0]
Qy=Q[1]


for i in range(1,n):
    
    if Px==Qx:
        lam=((3*(Px**2)+a)/(2*Py))
        lam=Fraction(lam).limit_denominator(1000)
        lam=lam.as_integer_ratio()
        lam1=lam[0]%p
        lam2=add(p,lam[1])
        lam3=(lam1*lam2)%p
        rx=(lam3**2-Px-Qx)%p
        ry=(lam3*(Px-rx)-Py)%p
    else:
        lam=((Qy-Py)/(Qx-Px))
        lam=Fraction(lam).limit_denominator(1000)
        lam=lam.as_integer_ratio()
        lam1=lam[0]%p
        lam2=add(p,lam[1])
        lam3=(lam1*lam2)%p
        rx=(lam3**2-Px-Qx)%p
        ry=(lam3*(Px-rx)-Py)%p
    Px=rx
    Py=ry


    print(lam3)
    R=(Px,Py)
    print("R=",R)
print("Final R=",R)    

#d=(0.5).as_integer_ratio()
#print(d)
