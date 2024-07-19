a,b=input().split()
a=int(a)
b=int(b)

while a<=b:
    if a%2==0:
         print(a, end=" ")
         a+=3
    else:
        print(a, end=" ")
        a*=2