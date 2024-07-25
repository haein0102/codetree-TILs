N=int(input())
x=0

while True:
    if N%2!=1:
        N=N//2
        x+=1
    else:
        break
print(x)