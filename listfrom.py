#slicing
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(l[::])
print(l[::2])
print(l[8::-2])
print(l[-1:1:-2])
print(l[:5:-2])
print(l[:-11:-2])
print(l[-3:1:-3])
print(l[-3:2:-3])
a=[1,2,3,4,[5,6,7,[8,9,10,11,12,13,14,[15,16,17,18,19,20,21,22,23,24],25,26,27,28,29],30,31,32,33],34,35,36,37]
print(a[4][3][-6][-2:2:-2])
print(a[4][-3::])