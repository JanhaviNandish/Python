#sum of even and odd num
num=[2,22,27,29,35,42,8,75,88]
sume=0
sumo=0
for i in num:
    if i%2==0:
        sume=sume+i
    else:
        sumo=sumo+i
print("sum of even",sume)
print("sum of odd",sumo)