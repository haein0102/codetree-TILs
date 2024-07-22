a,b=input().split()
a=int(a)
b=int(b)
cnt=0

for i in range(a,b+1):
    if i%2==0:
        cnt+=i
print(cnt)