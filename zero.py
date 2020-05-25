
from fractions import Fraction
import math as m
import random as rn
import functools as fn

def egcd(r1,r2):                #extended eucledian function
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
    
def sig_add(P,Q):               #point addition
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
    #print(R)
    return(R)

def add(P,Q,n):         #point addition and point doubling for n number of times
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

def padder(k):              #this function padds the string 
    asci=k
    l=len(asci)
    if (len(k)%32)!=0:
        asci.append('0')
        padder(asci)
    return asci

def splitter(gp):            #this function makes a list of lists
    gp=gp
    ngp=list()
    j=0
    passes=len(gp)/32
    for i in range(0,int(passes)):
        ngp.append(gp[j:j+32])
        j=j+32
    return ngp

def integer(ggp):           #string to integer form in grouping
    ggp=ngp
    agp=list()
    j=0
    for i in range(0,len(ggp)):
        gp=ngp[i]
        for k in range(0,len(gp)):
            gp[k]=int(gp[k])
        s=[str(l) for l in gp]
        gp=int("".join(s))
        agp.append(gp)
    return(agp)

def split(p):               #split Pm into co-ordinate form
    d=p
    d=list(str(d))
    #print('d=',d)
    a = d[0:len(d)//2] 
    b = d[len(d)//2 if len(d)%2 == 0
			    else ((len(d)//2)+1):] 
    
    for i in range(0, len(a)): 
        a[i] = int(a[i])
    for i in range(0, len(b)): 
        b[i] = int(b[i])
    #print(o)
    #print(u)
    
    strings1 = [str(integer) for integer in a]
    a_string1 = "".join(strings1)
    a = int(a_string1)
    #print(o)

    strings2 = [str(integer) for integer in b]
    a_string2 = "".join(strings2)
    b = int(a_string2)
    #print(u)
    p_m=(a,b)
    #print(" ")
    return p_m

def convert(list): 
      
    # Converting integer list to string list 
    s = [str(i) for i in list] 
      
    # Join list items using join() 
    res = int("".join(s)) 
      

    return(res)     
    

a = -3
b = 2455155546008943817740293915197451784769108058161191238065
nB = 28186466892849679686038856807396267537577176687436853369
p=6277101735386680763835789423207666416083908700390324961279
G = [60204628237568865675821348058752611191669876636884684818, 174050332293622031404857552280219410364023488927386650641]
Pb = [2803000786541617331377384897435095499124748881890727495642, 4269718021105944287201929298168253040958383009157463900739]
K=rn.randint(50,60)


k=''
st='National Institute of Technology,Manipur,795001 (English)' #input String
print("THE ORIGINAL STRING :",st)
print(" ")
for i in st:
   v=str(ord(i))
   k=k+v
print("ASCII value:",k)
k=list(k)

print(" ")
nk=padder(k)
print("THE PADDED ASCII VALUES{} AND ITS LENTGH {} ".format(nk,len(nk)))

print(" ")
ngp=splitter(nk)
print("THE FINAL GROUPS:")
#for i in ngp:
   # print(" ")
   # print(i)
print(ngp)

print(" ")
gp=integer(ngp)             #groups in integer format
print("Grouping:",gp)

print(" ")
kPb=add(Pb,Pb,K)
print("kPb=",kPb)

print(" ")
kG=add(G,G,K)
print("kG=",kG)

print(" ")
pm=list()
for i in range(0,len(gp)):  #split each element of group into co-ordinate format
    p=gp[i]
    p_m=split(gp[i])
    pm.append(p_m)
print("Pm= ",pm)

print(" ")
s=list()
r=list()
for i in range(0,len(gp)):
    enc=sig_add(pm[i],kPb)      #Encryption of each single input Pm
    r.append(enc)
    Cm=(kG,enc)             
    s.append(Cm)
print(" ")
print("Encrypted=",r)

print(" ")
print("Cm=",s)

lis=list()                  #Each Encrypted msg in single integer form
for i in range (0,len(r)):
    res = int(''.join(map(str, r[i])))
    lis.append(res)
    
print(" ")
print("list=",lis)

big_int=convert(lis)        #Joining the list to form single big integer
print(" ")
print("Big integer=",big_int)

big_int=list(str(big_int))
#print(big_int)

for i in range(0, len(big_int)): 
    big_int[i] = int(big_int[i])
#print(big_int)

encrypted = "".join([chr(c) for c in big_int])      #Encrypted Message
print("Encrypted Message= ",encrypted)
    


#nbkG=add(kG,kG,nB)
#print("nbkG=",nbkG)

#nbkGx=nbkG[0]
#nbkGy=-nbkG[1]
#new_nbkG=(nbkGx,nbkGy)
#print(new_nbkG)
    
    














    

