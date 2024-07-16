a_math, a_english=input().split()
b_math, b_english=input().split()
a_math=int(a_math)
a_english=int(a_english)
b_math=int(b_math)
b_english=int(b_english)

if a_math>b_math:
    print("A")
elif a_math<b_math:
    print("B")
elif a_math==b_math and a_english>b_english:
    print("A")
else:
    print("B")

#if a_math > b_math or (a_math == b_math and a_eng > b_eng):
#    print("A")
#else:
#    print("B")