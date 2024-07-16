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

print(min_value)