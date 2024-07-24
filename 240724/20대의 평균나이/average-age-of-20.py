cnt=0
sum_val=0

while True:
    n=int(input())
    if n>=30 or n<=19:
        print(f"{sum_val/cnt:.2f}")
        break
    else:
        cnt+=1
        sum_val+=n