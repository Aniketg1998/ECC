from fractions import Fraction
import random as rn
import math as m

def per(y,p):
    c=int(y)
    flag=0
    for i in range(1,c+1):
      if(y==(i*i)):
          flag=1
    return flag

def egcd(r1,r2):
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
    
def add(P,Q,n):
    Px=P[0]
    Py=P[1]
    Qx=Q[0]
    Qy=Q[1]
    #print('n',n)
    for i in range(1,int(n)):
        
        if Px==Qx:
            lam=((3*(Px**2)+a)/(2*Py))
            lam=Fraction(lam).limit_denominator(1000)
            lam=lam.as_integer_ratio()
            lam1=lam[0]%p
            lam2=egcd(p,lam[1])
            lam3=(lam1*lam2)%p
            rx=(lam3**2-Px-Qx)%p
            ry=(lam3*(Px-rx)-Py)%p
        else:
            lam=((Qy-Py)/(Qx-Px))
            lam=Fraction(lam).limit_denominator(1000)
            lam=lam.as_integer_ratio()
            lam1=lam[0]%p
            lam2=egcd(p,lam[1])
            lam3=(lam1*lam2)%p
            rx=(lam3**2-Px-Qx)%p
            ry=(lam3*(Px-rx)-Py)%p
        Px=rx
        Py=ry
        #print(lam3)
        R=(Px,Py)
      #  print(R)
    return(R)

def sig_add(P,Q):
    Px=P[0]
    Py=P[1]
    Qx=Q[0]
    Qy=Q[1]
    
    if Px==Qx:
            lam=((3*(Px**2)+a)/(2*Py))
            lam=Fraction(lam).limit_denominator(1000)
            lam=lam.as_integer_ratio()
            lam1=lam[0]%p
            lam2=egcd(p,lam[1])
            lam3=(lam1*lam2)%p
            rx=(lam3**2-Px-Qx)%p
            ry=(lam3*(Px-rx)-Py)%p
    else:
            lam=((Qy-Py)/(Qx-Px))
            lam=Fraction(lam).limit_denominator(1000)
            lam=lam.as_integer_ratio()
            lam1=lam[0]%p
            lam2=egcd(p,lam[1])
            lam3=(lam1*lam2)%p
            rx=(lam3**2-Px-Qx)%p
            ry=(lam3*(Px-rx)-Py)%p
    Px=rx
    Py=ry
    #print(lam3)
    R=(Px,Py)
    #  print(R)
    return(R)


a=int(input("enter positive value of a="))
b=int(input("enter positive value of b="))
p=int(input("enter positive value of p="))
l=list()

for x in range(0,p):
    #print("X=",x)
    y=((x**3)+(a*x)+b)%p
    while(per(y,p)!=1 and y<=(p*p)):
        y=y+p
    s=m.sqrt(y)
    y1=(-s)+p
    if y >= p**2:
        continue
    else:
        tup1=(x,s)
        #print(tup1)
        l.append(tup1)
        tup2=(x,y1)
        l.append(tup2)
        #print(tup2)
print("FINAL LIST=",l)

P=l[rn.randint(0,len(l)-1)]
print("P=",P)
Q=l[rn.randint(0,len(l)-1)]
print("Q=",Q)
G=l[rn.randint(0,len(l)-1)]
print("G=",G)
k=rn.randint(1,300)
#print("k=",k)
n=rn.randint(1,300)
#print("n=",n)
na=rn.randint(1,n-1)
#print("na=",na)
nb=rn.randint(1,n-1)
#print("nb=",nb)
Pm=l[rn.randint(0,len(l)-1)]
print("Message=",Pm)

Pa=add(G,G,na)
print("Public key of A=",Pa)

Pb=add(G,G,nb)
print("Public key of B=",Pb)

K1=add(Pb,Pb,na)
print("Secret key of A=",K1)

K2=add(Pa,Pa,nb)
print("Secret key of B=",K2)

kG=add(G,G,k)
#print("kG=",kG)

kPb=add(Pb,Pb,k)
#print("kPb=",kPb)

enc=sig_add(Pm,kPb)
print("Encrypted message=",enc)

Cm=(kG,enc)
print("Encrypted message with mask kG=",Cm)

nbkG=add(kG,kG,nb)
#print("nbkG=",nbkG)

nbkGx=nbkG[0]
nbkGy=-nbkG[1]
nbkG=(nbkGx,nbkGy)
print("Decryptor=",nbkG)

dec=sig_add(enc,nbkG)
print("Decrypted message=",dec)

