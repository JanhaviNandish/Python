i=20
mul=1
while mul:
    print(i)
    mul*=i
    if mul==8000:
        break
    print("we are in loop")
print(mul)
print("finished")