a,b=input().split()
a=int(a)
b=int(b)

if a%2==0 and b%2==0:
    for i in range(a+,b+2,2):
        print(i, end=" ")
else:
    for i in range(a,b+1,2):
        print(i, end=" ")