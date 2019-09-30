n=input()
for i in n:
    if i==i.upper():
        print(i.lower(),end=' ')
    elif i==i.lower():
        print(i.upper(),end=' ')
    else:
        print(i)
