
str=input("enter text message=")

h =([hex(ord(i)) for i in str]);
print("hexa form=",h)


s="".join(h)
print(s)
                
