#wap to remove duplicants from the given i/p string without usinf set().
s=input()
s=sorted(s)
s=list(s)
t=''
i=0
while i<len(s)-1:
    if s[i]!=s[i+1]:
        t+=s[i]
        i+=1
    else:
        i+=1
t+=s[-1]
print(t)
