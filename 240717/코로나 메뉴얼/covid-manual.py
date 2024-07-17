a1,a2=input().split()
b1,b2=input().split()
c1,c2=input().split()
a2=int(a2)
b2=int(b2)
c2=int(c2)

a_category = ''
b_category = ''
c_category = ''

if a1=="Y":
    if a2>=37:
        a_category ='A' 
    else:
        a_category ='C' 
else:
    if a2>=37:
        a_category ='B' 
    else:
        a_category ='D'

if b1=="Y":
    if b2>=37:
       b_category ='A' 
    else:
       b_category ='C' 
else:
    if b2>=37:
        b_category ='B' 
    else:
        b_category ='D'

if c1=="Y":
    if c2>=37:
        c_category ='A' 
    else:
        c_category ='C' 
else:
    if c2>=37:
        c_category ='B' 
    else:
        c_category ='D'

a_count = 0
if a_category == 'A':
    a_count += 1
if b_category == 'A':
    a_count += 1
if c_category == 'A':
    a_count += 1

if a_count>=2:
    print("E")
else:
    print("N")