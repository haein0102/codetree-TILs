n=int(input())

for i in range(1, n + 1):
    print('*' * i, end='\n\n')

# 감소하는 부분
for i in range(n - 1, 0, -1):
    print('*' * i, end='\n\n')