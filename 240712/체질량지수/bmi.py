h,w=input().split()
h=int(h)
w=int(w)

b=w//(h/100)**2
b=int(b)

print(b)
if b>=25:
    print("Obesity")