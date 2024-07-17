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



# a와 b를 비교한뒤, a가 b보다 크다면 a와 c를 비교하여 최댓값을 구합니다.
#if a >= b:
#    if a >= c:
#        print(a)
#    else:
#        print(c)

# a와 b를 비교한 결과가 나와있으므로, b와 c만 비교하여 최댓값을 구합니다.
#else:
#    if b >= c:
#        print(b)
#    else:        print(c)