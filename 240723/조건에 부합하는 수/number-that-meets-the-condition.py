a=int(input())
n=0
b=0

for i in range(1,a+1):
    if i%2==0 and i%4!=0:
        continue
    if i//8==n and n % 2 == 0:
        n+=1
        continue
    if i%7==b and b<4:
        b+=1
        continue
    print(i, end=" ")