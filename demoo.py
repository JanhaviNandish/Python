s=input()
s=sorted(s)
t=''
for i in s:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        t+=i
        while i<len(s)-1:
            if s[i]!=s[i+1]:
                t+=s[i]
                i+=1
            else:
                i+=1
        t+=s[-1]
    
print(t)


        
