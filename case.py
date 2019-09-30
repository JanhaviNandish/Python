#wap to swapcase without swapcase function
n = input()
for s in n:
 if s == s.upper():
    print (s.lower(),end='')
 elif s == s.lower():
    print (s.upper(),end='')
 else:
    print (s,end='')
