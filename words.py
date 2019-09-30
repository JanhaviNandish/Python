#remove multiple spaces in between the words, at begining and end of the words
#and give the count of words for the given string

def countWords(a):
    count=0
    i=0
    while i<len(a):
        if a[i]==' ' and a[i+1]!=' ':
            count+=1
            i+=1
        else:
            i+=1
    return(count+1)
s=input()
st=0
ed=0
i=0
while i<len(s):
    if s[i]!=' ':
        st=i
        #i+=1
        break
    else:
        i+=1
        
i=len(s)-1
while i>0:
    if s[i]!=' ':
        ed=i
       # i+=1
        break
    else:
        i-=1
d=s[st:ed-1]
print(countWords(d))
