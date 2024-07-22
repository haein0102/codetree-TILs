n=int(input())
sum_val=0
cnt=0

for i in range(n):
    number=int(input())
    sum_val+=number
    cnt+=1

print(f"{sum_val} {sum_val/cnt:.1f}")