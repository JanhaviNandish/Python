print("enter any number")
x=int(input())
if  x%3==0 and x%5==0:
    print("fuzzbuzz")
elif x%5==0:
    print("buzz")
elif x%3==0:
    print("fuzz")
else:
    print("get lost")