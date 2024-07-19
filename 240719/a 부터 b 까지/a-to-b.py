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
               

#for i in range (a, b+1):    <- 이런식은 왜 안되는지?
#        if i % 2 == 1:
#            print(i, end = " ")
#            i *= 2
#        elif i % 2 == 0:
#            print(i, end = " ")
#            i += 3