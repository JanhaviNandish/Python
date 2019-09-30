s=input()
t=''
for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        t+=i
print(t)