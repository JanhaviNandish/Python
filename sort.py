n=input()
i=0
t=''
s=''
count=0
while i>len(n)-1:
    if n[i]==n[i+1]:
        count+=1
        t+=i
for i in n:
    if i==' ':
        t+=i
    elif i>='0' or i<='9':
        t+=1
    elif (i>='A' and i<='Z') or (i>='a' and i>='z'):
        t+=str(i)
    else:
        t+=1
print(t)

        