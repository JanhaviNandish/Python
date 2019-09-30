y=list(range(1900,2000))
for i in y:
    if i%3==0 and i%5==0:
        print("FuzzBuzz")
    elif i%7==0 and (i%4==0 and i%100!=0 or i%400==0):
        print("unlucky number", end=' ')
    elif i%3==0:
        print("fuzz",end=' ')
    elif i%5==0:
        print("buzz",end=' ')
    elif i%7==0:
        print("complex number",end=' ')
    elif i%4==0 and i%100!=0 or i%400==0:
        print("leap year",end=' ')
    else:
        print(i)