#convert any data type to int
#binary
b="110"
print("data type of b:",type(b))

a=int(b) #always int is decimal base
print(a)
print("data type of a:",type(a))  

c=int(b,2) #convert binary to decimal wrt base 2
print(c)
print("dat type of c is",type(c))
print("*****************************")
#octal
d="11036"
print("data type of d:",type(d))

a=int(d) #always int is decimal base
print(a)
print("data type of a:",type(a))  

c=int(d,8) #convert octal to decimal wrt base 2
print(c)
print("dat type of c is",type(c))
print("**************************")
#hexa
b="110"
print("data type of b:",type(b))

a=int(b) #always int is decimal base
print(a)
print("data type of a:",type(a))  

c=int(b,16) #convert hexa to decimal wrt base 2
print(c)
print("dat type of c is",type(c))