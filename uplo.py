#case convert
k=input()
s=''
for n in k:
    
    if n>='a' and n<='z':
        s+=n.upper()
    elif n>='A' and n<='Z':
        s+=n.lower()
    else:
        s+=1
print(s)

