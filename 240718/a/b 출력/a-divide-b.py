a,b=input().split()
a=int(a)
b=int(b)

integer_part = a // b

# 소수 부분 구하기
remainder = a % b
decimal_part = ""

for i in range(20):
    remainder *= 10
    digit = remainder // b
    decimal_part += str(digit)
    remainder %= b

# 결과 출력
print(f"{integer_part}.{decimal_part}")