#ip:t2hi3s i3s 1my c2la2ss
#op:th*is5 *is3 my1 cl*ass4
n=input()
t=''
#ti=0
sum=0
for i in n:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            t+='*'
            t+=i
        else:
            t+=i
    elif i>='0' and i<='9':
        sum+=int(i)
    elif i==' ':
        t+=str(sum)+' '
        sum=0
t+=str(sum)+' '
print(t)