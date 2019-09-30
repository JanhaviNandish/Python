l=list(range(1,201))
l1=[]
def power(i):
    return i**3
for i in l:
    if(i%3==0):
        l1.append(power(i))
print(l1)

