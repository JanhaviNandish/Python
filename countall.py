#wap to print word count, vowel count, consonent count, space count,
#special charecter count, number count.
s=input().lower()
wc=0
vc=0
cc=0
sp=0
sc=0
nc=0
count=0
i=0
while i<len(s):
    if s[i]==' ':
        count+=1
        i+=1
    else:
        i+=1
wc=count+1
sc=count
i=0
while i<len(s):
    if s[i]>='a' and s[i]<='z':
        if s[i]=='a' or s[i]=='e'or s[i]=='i' or s[i]=='o' or s[i]=='u':
            vc+=1
            i+=1
        else:
            cc+=1
            i+=1
    elif s[i]>='0' and s[i]<='9':
        nc+=1
        i+=1
    elif s[i]!=' ':
        sp+=1
        i+=1
    else:
        i+=1
print('word count: ',wc)
print('space count: ',sc)
print('vowel count: ',vc)
print('consonent count: ',cc)
print('number count: ',nc)
print('special charecter count: ',sp)
    