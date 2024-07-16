#A_age, A_sex= input().split()
#B_age, B_sex=input().split()

#A_age=int(A_age)
#B_age=int(B_age)

#if (A_sex == 'M' or B_sex == 'M') and (A_age>=19 or B_age >=19):
#    print(1)
#else:
#    print(0)

# 첫 번째 사람의 정보 입력받기
age1, gender1 = input().split()
age1 = int(age1)

# 두 번째 사람의 정보 입력받기
age2, gender2 = input().split()
age2 = int(age2)

# 조건 판단 및 출력
if (age1 >= 19 and gender1 == 'M') or (age2 >= 19 and gender2 == 'M'):
    print(1)
else:
    print(0)