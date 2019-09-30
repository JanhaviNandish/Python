l=[1999,2000,2004,2020,2006,2010,2019]
for i in l:
    if i%4==0 and i%100!=0 or i%400==0:
        print("{0} is a leap year".format(i))
    else:
        print("{0} is not a leap year".format(i))