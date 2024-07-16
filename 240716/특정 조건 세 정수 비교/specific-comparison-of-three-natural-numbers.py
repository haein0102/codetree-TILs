a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if a <= b and a <= c:
    min_value = a
elif b <= a and b <= c:
    min_value = b
else:
    min_value = c

if a==min_value:
    print(1, end=" ")
else:
    print(0, end=" ")
    
if a==b==c:
    print(1, end=" ")
else:
    print(0, end=" ")