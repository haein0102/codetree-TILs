a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if a>=b>=c:
    print(a)
elif b>=a>=c:
    print(b)
else:
    print(c)