num=[2,22,27,29,35,42,8,75,88]
for i in num:
    if i%3==0 and i%5==0:
        print("fuzzbuzz",i)
    elif i%3==0:
        print("fuzz",i)
    elif i%5==0:
        print("buzz",i)
    else:
        print("getlost",i)