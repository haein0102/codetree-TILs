a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

# 최댓값을 찾기
if a >= b and a >= c:
    max_value = a
elif b >= a and b >= c:
    max_value = b
else:
    max_value = c

# 최댓값 출력
print(max_value)