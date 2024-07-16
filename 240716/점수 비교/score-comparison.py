a_Math,a_English=input().split()
b_Math,b_English=input().split()
a_Math=int(a_Math)
a_English=int(a_English)
b_English=int(b_English)
b_Math=int(b_Math)

if a_Math>b_Math and a_English>b_English:
    print(1)
else:
    print(0)