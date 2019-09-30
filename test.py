#print the second highest number
n=int(input())
l=[]
fbig=0
sbig=0
for i in range(n):
    x=input()
    l.append(x)
for i in l:
    if fbig<i:
        sbig=fbig
        fbig=i
    elif sbig<i and i!=fbig:
        sbig=i
print(sbig)