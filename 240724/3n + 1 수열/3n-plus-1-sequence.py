N=int(input())
cnt=0

while True:
    if N==1:
        print(cnt)
        break
    elif N%2==0:
        N=N//2
        cnt+=1
    elif N%2==1:
        N=(N*3)+1
        cnt+=1