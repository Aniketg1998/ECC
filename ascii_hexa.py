import binascii
def asciii(txt):
    a=''
    b=0
    for i in txt:
        conv=ord(i)
        b=conv
        b=str(b)
        a=a+b
        print(a)
    return a   
    
txt=str(input("Enter text:"))
asci=asciii(txt)
asci=int(asci)
print('ascii=',asci)

hexa=hex(asci)
print('hex=',hexa)
