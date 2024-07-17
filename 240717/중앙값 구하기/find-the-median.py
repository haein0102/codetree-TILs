a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if (a >= b and a <= c) or (a <= b and a >= c):
    median = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    median = b
else:
    median = c

print(median)