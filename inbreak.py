l=[1,2,3,4,5,6]
sum=0
for i in l:
    print(i)
    sum+=i
    if sum>=5:
        break
    print("we are in loop")
print("for loop outside")
print(sum)