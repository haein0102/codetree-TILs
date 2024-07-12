n=int(input())

if n>=3000:
    print("book")
elif n<1000:
    print("no")
else:
    print("mask")

#만약 코드가 if n >= 3000:
#	print("book");
#elif n >= 1000:
#	print("mask");
#else:
#	print("no"); 이렇게 되면 n이 4000 이런식으로 되면 if문이랑 elif문 동시에 성립해서 book이랑 mask가 동시에 나오는 건 아닌지?