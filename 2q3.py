#sample ip: this is my class
#op: this4 is2 my2 class5
n=input()
t=''
count=0
for i in n:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        t+=i
        count+=1
    elif i==' ':
        t+=str(count)+' '
        count=0
t+=str(count)
print(t)
        