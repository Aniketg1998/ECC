def padder(k): #this function padds the string 
    asci=k
    l=len(asci)
    if (len(k)%64)!=0:
        asci.append('0')
        padder(asci)
    return asci

def splitter(gp): #this function makes a list of lists
    gp=gp
    ngp=list()
    j=0
    passes=len(gp)/64
    for i in range(0,int(passes)):
        ngp.append(gp[j:j+64])
        j=j+64
    return ngp
def integer(ggp):
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

k=''
st='Python has features, which also support various concepts of functional programming language. ' #input String
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

gp=integer(ngp)
print("Grouping:",gp)
print(" ")



