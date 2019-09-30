l=list(range(500))
for i in l:
    if i%3==0 and i%5==0:
        print(i,end="\n\n")
    elif i%3==0:
        print(i)
    elif i%7==0:
        print("unlucky number")
    else:
        print(i,end=" ")