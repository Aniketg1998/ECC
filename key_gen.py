def per(y,p):
    c=int(y)
    flag=0
    for i in range(1,c+1):
      if(y==(i*i)):
          flag=1
    return flag
import math as m
a=int(input("enter positive value of a="))
b=int(input("enter positive value of b="))
p=int(input("enter positive value of p="))
for x in range(0,p):
    print("X=",x)
    y=((x**3)+(a*x)+b)%p
    while(per(y,p)!=1 and y<=(p*p)):
        y=y+23
    s=m.sqrt(y)
    y1=(-s)+p
    if y >= p**2:
        print("SQRT OUT OF BOUNDS")
        continue
    else:
        tup1=(x,s)
        print(tup1)
        tup2=(x,y1)
        print(tup2)
        
