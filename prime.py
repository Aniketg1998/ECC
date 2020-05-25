#for i in range(32769,65536):
    #if (i%2)!=0 and (i%3)!=0 and (i%5)!=0 and(i%7)!=0 and (i%11)!=0:
       # print(i)
    #else:
        #continue
integers = [1, 2, 3]

strings = [str(integer) for integer in integers]
a_string = "".join(strings)
an_integer = int(a_string)

print(an_integer)
