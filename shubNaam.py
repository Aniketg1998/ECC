import binascii
import random
import string
def asciii(txt):
    a=''
    b=0
    for i in txt:
        conv=ord(i)
        b=conv
        b=str(b)
        a=a+b
        #print(a)
    return a   
    
txt="heelloo this is aniket and i love programming"
asci=asciii(txt)
asci=int(asci)
print("ascii=",asci)
asci=str(asci)

N=len(asci)%16
if (len(asci)%16)!=0:
    new_asci=asci.ljust((16-N)+len(asci),'0')
else:
    new_asci=asci
print("new_asci=",new_asci)
new_asci=list(new_asci)
count=0
gp=list()
varl=list()
j=0
for i in new_asci:
     if count<16:
            gp.append(i)
            count=count+1
        
        
     else:
        print(len(gp))
        varl.append(gp)
        #print(varl)
        gp.clear()
        
        count=0
        
        
    
