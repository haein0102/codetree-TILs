A_age, A_sex= input().split()
B_age, B_sex=input().split()

A_age=int(A_age)
B_age=int(B_age)

if (A_sex == 'M' or B_sex == 'M') and (A_age>=19 or B_age >=19):
    print(1)
else:
    print(0)