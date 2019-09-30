#input: 1hell2o wo6el7d
#output: hello3 world13

s=input()
t=''
sum=0
for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        t+=i
        
    elif i>='0' and i<='9':
        sum+=int(i)
        
    elif i==' ':
        t+=str(sum)+' '
        sum=0
print(sum)
t+=str(sum)
print(t)
