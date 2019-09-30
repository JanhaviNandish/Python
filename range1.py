l=list(range(358))
for i in l:
    if i%3==0 and i%5==0:
        print("{0}fuzzbuzz".format(i))
    elif i%3==0:
        print("{0}fuzz".format(i))
    elif i%5==0:
        print("{0}buzz".format(i))
    else:
        print(i)

