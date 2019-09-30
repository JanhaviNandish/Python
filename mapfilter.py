l=list(range(1,201))

l2=list(map(lambda x:x**5,list(filter(lambda x:x%5==0,l))))
print(l2)