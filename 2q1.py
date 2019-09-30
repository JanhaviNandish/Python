#wap to find the number of occarances
n=input()
n=sorted(n)
i=0
count=1
t=''
s=''
while i<len(n)-1:
    if n[i]==n[i+1]:
        count+=1
        i+=1
    else:
        print(n[i],'comes in',count,'times')
        count=1
        i+=1
t+=n[-1]
s+=str(count)
print(t,'comes in',s,'times')