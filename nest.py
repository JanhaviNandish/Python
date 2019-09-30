n=int(input())
l=[]
for i in range(n):
    a=[]
    name=input()
    grade=float(input())
    a.append(name)
    a.append(grade)
    l.append(a)
l.sort()
k=0
for i in range(n):
    if l[i][0]>l[0][0]:
        k=i
        break
for i in range(n):
    if l[k][0]==l[i][0]:
        print(l[i][1])