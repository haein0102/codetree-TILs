n=int(input())
sum_val=0

for i in range(n):
    number=int(input())
    if number%3==0 and number%2!=0:
        sum_val+=number
    
print(sum_val)